# Real-Time-Stock-Price-Scraper
<h2>Enviroment</h2><br>
<ul>
  <li> OS: Windows 10 </li>
  <li> Platform: Python 3</li>
  <li> Libraries:
    <ul style="list-style-type:disc;">
      <li>BeautifulSoup</li>
      <li>requests</li>
      <li>csv</li>
      <li>time</li>
      <li>threading</li>
    </ul>
  </li>
</ul>

<h2> How does it works </h2><br>
<ol>
  <li>It scraps the real time stock data from the webpage: 'https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9'</li>
  <li>An alert is created for the user if the change in %CHG lowers or rises 2%</li>
  <li>In every 30 second time interval, the data is scraped from this webpage</li>
  <li>At the end of data scraping(the scraping is continuous until user stops it) a CSV file is created with each company's stock and its other informations.</li>
</ol>
