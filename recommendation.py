import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

def recommendation():

    df = pd.read_csv("/home/balaji/Downloads/temp_bq_data/hackathon1_data.csv")

    considered_product_id = list(df["product_id"].value_counts().sort_values(ascending=False).index.values[0:100])
    print(len(considered_product_id))

    df = df.loc[df["product_id"].isin(considered_product_id)]

    recommend_dataframe = df[["product_id", "customer_id"]]
    del df

    recommed_dataframe_dummies = pd.get_dummies(recommend_dataframe["product_id"])
    recommend_dataframe = pd.concat([recommend_dataframe, recommed_dataframe_dummies], axis=1)
    del recommed_dataframe_dummies

    recommend_dataframe = recommend_dataframe.groupby(by="customer_id", as_index=False).sum()

    sparse_recommend = recommend_dataframe
    del recommend_dataframe

    model = NearestNeighbors(metric="cosine", n_neighbors=20)
    model.fit(sparse_recommend)
    results = model.kneighbors(sparse_recommend)
    print(results[1])
    final = pd.DataFrame(results[1])

    model = NearestNeighbors(metric="jaccard", n_neighbors=20)
    model.fit(sparse_recommend)
    results = model.kneighbors(sparse_recommend)
    print(results[1])
    final1 = pd.DataFrame(results[1])
    final = pd.concat([final, final1], axis=1)

    print(final)

    neighbors = pd.DataFrame()
    for row in range(final.shape[0]):
        current_custom_ind = final.ix[row:row, 0:0][0][row]
        lis  = []
        final1 = pd.DataFrame()
        for col in final.columns.values:
            if col == 0:
                continue
            neigh_customer = final.ix[row:row, col:col][col][row]
            lis.append(neigh_customer)
            final1 = final1.append(sparse_recommend.ix[neigh_customer:neigh_customer, 2:])

        lis  = list(final1.sum(axis=0).sort_values(ascending=False).index)
        lis.append(current_custom_ind)



        neighbors = neighbors.append(pd.DataFrame([lis]))


    neighbors.to_csv("/home/balaji/Downloads/temp_bq_data/hackathon_data1.csv", index=False)








    # model_jac = NearestNeighbors(metric="jaccard", n_neighbors=20)
    # model_jac.fit(sparse_recommend)
    # results = model_jac.kneighbors(sparse_recommend)
    # print(results[1])
    # final1 = pd.DataFrame(results[1])
    #
    # for row in range(final.shape[0]):
    #      print(set(final.ix[row:row])&(final1.ix[row:row]))






    final.to_csv("/home/balaji/Downloads/temp_bq_data/neighbors.csv", index=False)




def return_neighbors(id):
    #print(int(id)+10)
    df = pd.read_csv("final_neighbors.csv")
    #print(df.head(5))
    df = df.ix[df["customer_id"]==int(id), 0:5]

    return  df


if __name__ == "__main__":
    recommendation()






