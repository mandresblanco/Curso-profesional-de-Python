from typing import Dict, List, Tuple

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
    'Argentina': 1,
    'Mexico': 2,
    'Colombia': 3
}
countries: List[Dict[str, int]] = [
    {
        'name': 'Argentina',
        'people': '450000'
    },
    {
        'name': 'Mexico',
        'people': '500000'
    },
    {
        'name': 'Colombia',
        'people': '150000'
    }
]
print(countries)
