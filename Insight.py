from matplotlib import pyplot as plt
from Criptocurrency import Criptocurrency
from DataLoader import URL_COINBASE

class Insight:
    """
      Module for data insight. It is intended to show a plot and a text resume with market cap information
      """

    @staticmethod
    def plot_marketcap_distribution(data: list[Criptocurrency]):
        """
        Method to generate a plot of market capitalization vs criptocurrencies
        :param data: Reference data from where the criptocurrencies are obtained
        """

        # Get date of last update
        date_of_last_update = data[0].last_updated.strftime('%Y-%m-%d')

        #Get data to show in the bar plot
        marketcap_list = list(Criptocurrency.market_cap/1000000000 for Criptocurrency in data)
        slug_list = list(Criptocurrency.slug for Criptocurrency in data)

        #create the plot
        plt.clf()
        plt.figure(figsize=(10, 10.5))
        plt.bar_label(plt.bar(slug_list, marketcap_list, color='maroon', width=0.7, label='marketcap_list') , label_type='edge', fmt = '%5.1f')
        plt.ylabel('Market capitalization (billions)')
        plt.title('Market capitalization main criptocurrencies in billions (' + str(date_of_last_update) + ')')
        plt.grid(False)
        plt.xticks(rotation=45, ha='right')
        plt.savefig('bar_marketcap.png')
        plt.show()
        plt.close()

    @staticmethod
    def create_resume(data: list[Criptocurrency]):
        """
        Method to generate a resume of market capitalization of the Top 5 criptocurrencies
        :param data: Reference data from where the criptocurrencies are obtained
        """
        #Total sum for criptocurrencies market capitalization (billiions of euros)
        total_sum_marketcap = 0
        for cripto in data:
            total_sum_marketcap += cripto.market_cap
        total_sum_marketcap = total_sum_marketcap / 1000000000

        #Function to order data by market capitalization
        def sort_by_marketcap ( criptocurrency: Criptocurrency):
            return criptocurrency.market_cap

        #Data order by function
        data.sort(reverse=True, key = sort_by_marketcap)

        #Get date of last update
        date_of_last_update = data[0].last_updated.strftime('%Y-%m-%d')

        #Create dynamic resume top 5 criptocurrencies by market capitlization
        text = "Resume of the Top 5 criptocurrencies by market capitalization " + '\n'
        text += "Collected %d instances from %s" % (len(data), URL_COINBASE) + '\n'
        text += "Date of last update: %s " % date_of_last_update + '\n'

        for id in range(0, 5):
            criptocurrency_name = data[id].name
            criptocurrency_marketcap = data[id].market_cap / 1000000000
            perc_criptocurrency_marketcap = (criptocurrency_marketcap / total_sum_marketcap) * 100
            criptocurrency_price = data[id].eur_price

            text += "-" * 40 + '\n'
            text += str(id+1) + "° %s \n" % criptocurrency_name
            text += "# Market Cap.: %5.1f billions (euros)\n" % criptocurrency_marketcap
            text += "%% Market Cap.: %5.1f %%\n" % perc_criptocurrency_marketcap
            text += "Price by unit: %5.0f (euros)\n" % criptocurrency_price

        return text

