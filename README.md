# tv-tracker

There are plenty of tv show tracker apps out in the wild but I haven't found one that satisfies the requirements I have. 
- No social options
- Clean, minimal UI (subjective of course)
- Export options (CSV, JSON, etc.)

I'll be updating this README file throughout the process but as of right now, this is my current roadmap:
1. I'll be starting by utlizing [TheTVDB](https://thetvdb.com) for all show metadata and scraping the site using BeautifulSoup within Python to grab all the necessary show information
2. I'll then be creating a Web UI that's connected to a database that allows users to enter in a show and which episodes they've watched
3. TBD