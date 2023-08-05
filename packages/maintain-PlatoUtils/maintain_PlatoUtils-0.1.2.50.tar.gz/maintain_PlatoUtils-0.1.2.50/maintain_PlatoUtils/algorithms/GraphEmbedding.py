
import networkx as nx
import tensorflow as tf

import stellargraph as sg
from stellargraph import datasets,IndexedArray
from stellargraph.layer import GraphSAGE, link_classification, HinSAGE,DeepGraphInfomax
from sklearn.model_selection import train_test_split
from stellargraph.data import UnsupervisedSampler,BiasedRandomWalk
from stellargraph.mapper import Node2VecNodeGenerator,Node2VecLinkGenerator
from stellargraph.layer import Node2Vec

def GraphEmbedding(gClient,subGraph=[{"head":{"type":"Company","keyAttr":"CompanyName"},
                                        "tail":{"type":"Field","keyAttr":"FieldName"},
                                        "edgeType":["belongTo"]}],space="post_skill_school_ianxu",model="DeepWalk",
                    batch_size=128):
    if len(subGraph)>0:
        gClient.execute_query("USE {}".format(space))
        totalHtDfList=[]
        for triItem in subGraph:
            headType=triItem["head"]["type"]
            headKeyAttr=triItem["head"]["keyAttr"]
            tailType=triItem["tail"]["type"]
            tailKeyAttr=triItem["tail"]["keyAttr"]
            if len(triItem["edgeType"])>0:
                edgeTypeGroupStr=",".join(triItem["edgeType"])
            else:
                edgeTypeGroupStr="*"
            htDfItem=wrapNebula2Df(gClient.execute_query("LOOKUP ON {headType} WHERE {headType}.{headKeyAttr}!='不可能的名字'|\
                                    GO FROM $-.VertexID OVER {edgeTypeGroup} YIELD \
                                        $^.{headType}.{headKeyAttr} AS srcName,\
                                        $$.{tgtType}.{tgtKeyAttr} AS tgtName".format(
                                            headType=headType,headKeyAttr=headKeyAttr,
                                            tailType=tailType,tailKeyAttr=tailKeyAttr,
                                            edgeTypeGroup=edgeTypeGroupStr
                                        )))
            if htDfItem.shape[0]>0:
                htDfItem.dropna(inplace=True)
                totalHtDfList.append(htDfItem)
        totalHtDf=pd.concat(totalHtDfList)
        totalHtList=totalHtDf.values.tolist()
        
        random.seed(15)
        totalG=nx.from_edgelist(totalHtList)
        for nodeItem in totalG.node:
            totalG.node[nodeItem]["feature"]=np.random.random([1,128])
        if model=="DeepWalk":
            walk_number = 100
            walk_length = 5
            
            totalSGG=sg.StellarGraph.from_networkx(totalG, node_features="feature")
            walker = BiasedRandomWalk(
                        totalSGG,
                        n=walk_number,
                        length=walk_length,
                        p=1,q=1
                    )
            unsupervised_samples = UnsupervisedSampler(totalSGG, nodes=list(totalSGG.nodes()), walker=walker)
            generator = Node2VecLinkGenerator(totalSGG, batch_size)
            emb_size = 128
            node2vec = Node2Vec(emb_size, generator=generator)
            x_inp, x_out = node2vec.in_out_tensors()
            prediction = link_classification(
                output_dim=1, output_act="sigmoid", edge_embedding_method="dot"
            )(x_out)
            
            node2VecModelClassfier = tf.keras.Model(inputs=x_inp, outputs=prediction)

            node2VecModelClassfier.compile(
                optimizer=tf.keras.optimizers.Adam(lr=1e-3),
                loss=tf.keras.losses.binary_crossentropy,
                metrics=[tf.keras.metrics.binary_accuracy],
            )
            
            history = node2VecModelClassfier.fit(
                generator.flow(unsupervised_samples),
                epochs=15,
                verbose=1,
                use_multiprocessing=False,
                workers=4,
                shuffle=True,
            )
            
            x_inp_src = x_inp[0]
            x_out_src = x_out[0]
            embedding_model = tf.keras.Model(inputs=x_inp_src, outputs=x_out_src)
            node_gen = Node2VecNodeGenerator(totalSGG, batch_size).flow()
            node_embeddings = embedding_model.predict(node_gen, workers=4, verbose=1)
            
            nodeList=list(totalSGG.nodes())
            nodeEmbedDict=dict(list(zip(nodeList,node_embeddings.tolist())))
            
            return embedding_model,nodeEmbedDict
            
    return {}

