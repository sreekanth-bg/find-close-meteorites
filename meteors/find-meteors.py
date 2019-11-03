import requests
import math

###function to find the distance between 2 points (lat, long) in kms
def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2
    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_distance(list):
    return list.get('distance', math.inf)

if __name__ ==if __name__ == "__main__":
    m_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json', verify = True)
    m_data = m_resp.json()

    my_loc = (12.9716, 77.5946)

    for m in m_data:
        if 'reclat' not in m or 'reclong' not in m: continue
        m['distance'] = calc_dist(float(m['reclat']), float(m['reclong']), my_loc[0], my_loc[1])

    m_data.sort(key = get_distance)

    print(m_data[0:10])