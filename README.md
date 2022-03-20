<h3>YouTube Wrapped - A Python YouTube Music History Analytics</h3>
<br>A Python YouTube History Analytics, which reads your history data you get from Google and provide analytics about your YouTube history, specifically reviewing a user's listening habits 

<h3>Requirements</h3>
<ul>
<li>upgrade pip in pycharm ide using 'python -m pip install --upgrade pip'</li>  
  <li>install pandas package in pycharm ide using 'pip install pandas'</li>  
<li>A data downloaded from Google History (You can download from <a href="https://takeout.google.com/settings/takeout">Google History</a>)</li>
<li>Download history for YouTube and Searches. Select None from top and select YouTube and Serches</li>
</ul>

<h3>How To Use -- From Original Open Source Project</h3>
<ul>
<li>After downloading data from Google, unzip it.From YouTube Takeout folder copy YouTube->history folder and paste where the script is located</li>
<li>Same, from the Searches takeout folder copy the Searches folder and paste where the scrpt is located</li>
<li>Running without parameters will execute for both YouTube and Google Searches</li>
<li>Pass --y Y for running the script on YouTube data</li>
<li>Pass --g G for running the script on Google Searches data</li>
<li>It provide output in the csv files in the working directory</li>
</ul>

<h5>For queries or issues, feel free to contact or open an <a href="https://github.com/srcecde/google-youtube-history-analytics/issues">issue</a></h5>


