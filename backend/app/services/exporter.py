import pandas as pd

def export_to_csv(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def export_to_gpx(data, path):
    from gpxpy import gpx
    gpx_file = gpx.GPX()
    track = gpx.GPXTrack()
    gpx_file.tracks.append(track)
    segment = gpx.GPXTrackSegment()
    track.segments.append(segment)

    lat, lon = 55.7558, 37.6176  # начальная точка (можно задать)
    for point in data:
        segment.points.append(gpx.GPXTrackPoint(lat, lon, elevation=point["voltage"]))
        lat += 0.0001  # симуляция движения
    with open(path, "w") as f:
        f.write(gpx_file.to_xml())