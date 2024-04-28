# Summary funtion:
def abstract(url:str):
    from newspaper import Article
    # Create article
    article = Article(url)

    # Processing
    article.download()
    article.parse()
    article.nlp()

    # SUmmary
    summary = article.summary
    return summary