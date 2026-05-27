import json

FIXTURES_PATH = '/sessions/ecstatic-sweet-meitner/mnt/moving-light-db/src/fixtures.json'
CDN_BASE = 'https://cdn.aws.robe.cz/v1/image/resize/'
CDN_SUFFIX = '?width=452&height=452&fit=cover&withoutEnlargement=false'

# Map of fixture ID -> CDN hash
IMAGE_HASHES = {
    32: 'e2bc84495f13fc1251b5151cbc3313c6145b2d23',
    33: '401bff822913a8182209a6ef40c594071b9596c2',
    34: 'd4461d4132761f8bbc9c36bccbf9689594769daf',
    35: '31094cbf1d62e0dc46a9b410951c88980134becf',
    36: '9428ce42577164fa81a1201c0d58951599e7632c',
    37: 'cf5f5663bcc52116c460cd120ec31283ac7c867e',
    38: '90b188c23102fa0d21a98569f6b475535194d7b5',
    39: '30cea14efb6f539abb3d297a63aa28ad574d10c4',
    40: '422fbc138a8a68463837f9885cdfbffbc5076d0a',
    41: '0bcea92b0cebedb204ea70e82f032e4c6eb36612',
    42: '5db8a18088ad5fb16a75442595d5aa0a16e8eb83',
    43: '1bd122c99b2ec5239398fdfd9e73d77845dca4fd',
    44: 'd3a00b24e6fe3b815eb823da3ac2ddcdc6745713',
    45: '522fc31d583c077fe618dc267176f88d429255c2',
    46: '025ed591ad67ff06e9dd82b461e0c345ba595d4a',
    82: '3986c3f7906087b2c94ddd5591b57adfd66bc99e',
    83: '371252fca4e93281166480433c3fbbc5635c6c8e',
    84: '7c16e7d0f45129d3a4fc9e6be99a5f1a32e0e115',
    85: '03a8550efee31feac02a46950ddcde07b3317425',
    86: '94eb121bd9c63cc7c94442fc5bc160c897de02c4',
    87: 'bacf4d213ec3c79f0b0fbc9128588eea91297efa',
    88: '6c9de341cb1ae82efd1cbaa4693d7540565e81c6',
    112: '0d779a8285c7afd295ab8119df8a6b6b0062a4cc',
    113: '3db48374a321b2e5ef40ad95d3890a6c11b51035',
    114: '3c29fbf541143e8c7fc95072204b3b4db592ef95',
    160: '1ca93714d4f1af28aaf570958b2d99598c31aa94',
    161: 'd017cced42e33d41104c891055714cc77a84a0be',
    162: 'ba1c13388d90cb6dc65ab3b71a43603e6f22b84a',
    163: 'b110201c5d13303d9ca602ad6f137b36f12498ff',
    164: '250becbab29bfc7708047c584a64745a4b30a0a9',
    # 176 and 177: pages return "Whoops" error - no images available
}

with open(FIXTURES_PATH, 'r') as f:
    fixtures = json.load(f)

updated = 0
for fixture in fixtures:
    fid = fixture.get('id')
    if fid in IMAGE_HASHES:
        url = CDN_BASE + IMAGE_HASHES[fid] + CDN_SUFFIX
        old_url = fixture.get('imageUrl', '')
        if old_url != url:
            fixture['imageUrl'] = url
            updated += 1
            print(f"  Updated ID {fid}: {fixture.get('model', 'unknown')}")
        else:
            print(f"  Already set ID {fid}: {fixture.get('model', 'unknown')}")

with open(FIXTURES_PATH, 'w') as f:
    json.dump(fixtures, f, indent=2, ensure_ascii=False)

print(f"\nDone. Updated {updated} fixtures.")
print(f"Skipped IDs 176 (iSpiider X) and 177 (iFORTE LTX FollowSpot) - pages return errors.")
