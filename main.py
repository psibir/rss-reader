
# CLI RSS reader for Northwest Arkansas

import feedparser
import pyshorteners
import tldextract


# Reads a list of URLs from a file
def read_urls(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
    return [line.strip() for line in lines]


# Gets the RSS feed from a URL
def get_rss_feed(url):
  # Parse the RSS feed using the feedparser library
  feed = feedparser.parse(url)

  # Print the feed title and number of entries
  print("\n" + "="*50)
  print(feed.feed.title)
  print("="*50 + "\n")
  
  # Print the title, summary, and shortened link for each entry
  for entry in feed.entries:
    print("\n" + "-"*50)
    print(entry.title)
    print("-"*50)
    print(entry.summary)
    
   # Use the tldextract library to extract the domain name from the link URL
    domain = tldextract.extract(entry.link).domain
    print("Source:", domain)

    # Use the pyshorteners library to shorten the link URL
    s = pyshorteners.Shortener()
    shortened_link = s.tinyurl.short(entry.link)
    print("Link:", shortened_link)


def main():
    urls = read_urls('urls.txt')
    for url in urls:
        get_rss_feed(url)


main()
