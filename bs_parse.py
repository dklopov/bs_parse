import json
import time

profile_id = 2703357
while profile_id >= 2700000:
    connect_profile_id = http.client.HTTPSConnection("main.v2.beatstars.com")
    connect_profile_id.request("GET", "/musician?id=" + str(profile_id) + "&fields=profile,stats,email")
    response = connect_profile_id.getresponse()
    data_profile_id = response.read().decode("utf-8")
    data_json_profile_id = json.loads(data_profile_id)

    profile_id_display_name = data_json_profile_id['response']['data']['profile']['display_name']
    profile_id_user_type = data_json_profile_id['response']['data']['profile']['user_type']
    profile_id_user_contents_tracks = data_json_profile_id['response']['data']['user_contents']['tracks']
    profile_id_user_stats_plays = data_json_profile_id['response']['data']['stats']['plays']
    profile_id_user_email = data_json_profile_id['response']['data']['email']

    parse_result = str(profile_id) + ';' + profile_id_display_name + ';' + profile_id_user_type + ';' + str(
        profile_id_user_contents_tracks) + ';' + str(profile_id_user_stats_plays) + ';' + profile_id_user_email

    with open(r"result", "a") as file:
        file.write(parse_result + '\n')
    profile_id = profile_id - 1
    time.sleep(2)
