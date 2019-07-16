from xbmcswift2 import Plugin, xbmcgui
from resources.lib import voiceswithvision

plugin = Plugin()

URL = "https://archive.wpfwfm.org/getrss.php?id=voiceswdiocoop"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/voices-vision2.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/voices-vision2.jpg"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = voiceswithvision.get_soup(URL)
    
    playable_podcast = voiceswithvision.get_playable_podcast(soup)
    
    items = voiceswithvision.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = voiceswithvision.get_soup(URL)
    
    playable_podcast1 = voiceswithvision.get_playable_podcast1(soup)
    
    items = voiceswithvision.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
