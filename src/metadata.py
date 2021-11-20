team_color = {
    'RCB' :'#db1316',
    'CSK' : '#fdb913',
    'DC' : '#2561AE',
    'GL' : 'purple',
    'KKR' :'#391F5C',
    'PBKS':'#dd1212',
    'Kochi' : '#b603fc',
    'MI' :'#004587',
    'PWI' : '#2b2e33',
    'RPS' : 'black',
    'RR' : '#FF4081',
    'SRH' : '#fb653f'
}

alt = 1
def stage_score(row, team_code):
    global alt
    alt += 1
    if 'Eliminator' in row['stage'] or '3Rd Place Play-Off' in row['stage'] or 'Elimination Final' in row['stage']:
        return 7*((-1)**alt)
    if 'Match' == row['stage'].split(' ')[1]:
        return 6*((-1)**alt)
    if 'Qualifier 2' in row['stage'] or '1St Qualifying Final' in row['stage']:
        return 9*((-1)**alt)
    if 'Qualifier 1' in row['stage'] or '2Nd Qualifying Final' in row['stage']:
        return 8*((-1)**alt)
    if 'Semi-Final' in row['stage']:
        return 7.5*((-1)**alt)
    if 'Final' in row['stage']:
        if row['winner'] != team_code:
            return 9.5*((-1)**alt)
        return 10*((-1)**alt)
    return 4*((-1)**alt)



