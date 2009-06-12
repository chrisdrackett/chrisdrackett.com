from pylast import pylast

def sync_tracks(*args, **kwargs):
    try:
        tree = ET.parse(urllib.urlopen("http://ws.audioscrobbler.com/1.0/user/drackett/weeklytrackchart.xml"))
        x = tree.getroot()
        
        if not WeeklyUpdate.objects.filter(ident=x.attrib.get('from')):
            global_id = x.attrib.get('from')
            for track in x:
                try:
                    test = Artist.objects.get(mbid=track.find('artist').attrib.get('mbid'))
                except Artist.DoesNotExist:
                    a = Artist(
                        name = track.find('artist').text,
                        mbid = track.find('artist').attrib.get('mbid'),
                    )
                    a.save()
                try:
                    test = Track.objects.get(url=track.find('url').text)
                except Track.DoesNotExist:
                    t = Track(
                        name = track.find('name').text,
                        artist = Artist.objects.get(mbid=track.find('artist').attrib.get('mbid')),
                        url = track.find('url').text,
                    )
                    t.save()
                u = WeeklyUpdate(
                        track = Track.objects.get(url=track.find('url').text),
                        position = track.find('chartposition').text,
                        playcount = track.find('playcount').text,
                        ident = global_id,
                )
                u.save()
        return True
    except:
        return False