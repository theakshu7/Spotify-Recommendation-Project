import json
import matplotlib.pyplot as plt

def main():

    danceability = []
    valence = []
    energy = []
    acousticness = []
    liveness = []
    speechiness = []

    f = open('data/spotify_songs.json', encoding='utf8')
    data = json.load(f)

    for i in data:
        danceability.append(i['danceability'])
        valence.append(i['valence'])
        energy.append(i['energy'])
        acousticness.append(i['acousticness'])
        liveness.append(i['liveness'])
        speechiness.append(i['speechiness'])

    data = [danceability, valence, energy, acousticness, liveness, speechiness]

    fig = plt.figure(figsize=(15,10))

    ax = fig.add_subplot()

    bp = ax.boxplot(data, showfliers=False)
    ax.set_xticklabels(['Danceability', 'Valence', 'Energy', 'Acousticness', 'Liveness', 'Speechiness'])
    plt.title('Dataset Song Features')
    plt.show()

if __name__ == '__main__':
    main()