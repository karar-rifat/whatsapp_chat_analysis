from urlextract import URLExtract
from wordcloud import WordCloud

extract = URLExtract()


def fetch_starts(selected_user, df):
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # fetch number of message
    num_messages = df.shape[0]

    # fetch total number of words
    words = []
    for message in df["message"]:
        words.extend(message.split())

    # fetch number of media chat
    num_media_messages = df[df["message"] == "<Media omitted>\n"].shape[0]

    # fetch number of links shared
    links = []
    for message in df["message"]:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    x = df["user"].value_counts().head()
    df = (
        round((df["user"].value_counts() / df.shape[0]) * 100, 2)
        .reset_index()
        .rename(columns={"index": "name", "user": "percent"})
    )
    return x, df


# create wordcloud
def create_wordcloud(selected_user, df):
    # f = open("stop_hinglish.txt", "r")
    # stop_words = f.read()

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # temp = df[df["user"] != "group_notification"]
    # temp = temp[temp["message"] != "<Media omitted>\n"]

    # def remove_stop_words(message):
    #     y = []
    #     for word in message.lower().split():
    #         if word not in stop_words:
    #             y.append(word)
    #     return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    # temp["message"] = temp["message"].apply(remove_stop_words)
    # df_wc = wc.generate(temp["message"].str.cat(sep=" "))
    df_wc = wc.generate(df["message"].str.cat(sep=" "))
    return df_wc
