import os
from DataLoader import DataLoader, CACHE_FILE_NAME
from Insight import Insight

if __name__ == "__main__":

    #Import data from api call or from cache file
    if os.path.exists(CACHE_FILE_NAME):
        #Import data from json file
        data = DataLoader.import_data_from_json()
    else:
        # Import data from api
        data = DataLoader.import_data_from_api()

        # Export data from api to json file
        DataLoader.export_data_to_json(data)

    #Convert data to criptocurencies format based on the class "Criptocurrency"
    criptocurrencies_list = DataLoader.convert_to_criptocurrency(data)

    #Create a text resume
    print(Insight.create_resume(criptocurrencies_list))

    #Plot marketcap data in a bar chart
    Insight.plot_marketcap_distribution(criptocurrencies_list)
    print("You can see a bar plot file image with the main cripcocurrencies in your current directory!!")
    print("-" * 80 + '\n')



