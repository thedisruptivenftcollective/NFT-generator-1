layers = [
    {
        "name": "Background",
        "values": ["Blue", "Orange", "Purple", "Red", "Yellow"],
        "trait_path": "./layers/background",
        "filename": ["blue", "orange", "purple", "red", "yellow"],
        "weights": [0.9, 0.025, 0.025, 0.025, 0.025]
    },
    {
        "name": "Foreground",
        "values": ["Python Logo", "avatar"],
        "trait_path": "./layers/foreground",
        "filename": ["logo", "avatar"],
        "weights": [0.5, 0.5]
    },
    {
        "name": "Branding",
        "values": ["A Name"],
        "trait_path": "./layers/text",
        "filename": ["text"],
        "weights": [1]
    }
]

name = "NFT #"
