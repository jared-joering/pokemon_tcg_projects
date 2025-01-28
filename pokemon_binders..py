sets_data = [
    ("Base Set", 102),
    ("Jungle", 64),
    ("Fossil", 62),
    ("Base Set 2", 130),
    ("Team Rocket", 83),
    ("Gym Heroes", 132),
    ("Gym Challenge", 132),
    ("Neo Genesis", 111),
    ("Neo Discovery", 75),
    ("Neo Revelation", 66),
    ("Neo Destiny", 113),
    ("Legendary Collection", 110),
    ("Expedition Base Set", 165),
    ("Aquapolis", 186),
    ("Skyridge", 182),
    ("EX Ruby & Sapphire", 109),
    ("EX Sandstorm", 100),
    ("EX Dragon", 100),
    ("EX Team Magma vs. Team Aqua", 97),
    ("EX Hidden Legends", 102),
    ("EX FireRed & LeafGreen", 116),
    ("EX Team Rocket Returns", 111),
    ("EX Deoxys", 108),
    ("EX Emerald", 107),
    ("EX Unseen Forces", 145),
    ("EX Delta Species", 114),
    ("EX Legend Maker", 93),
    ("EX Holon Phantoms", 111),
    ("EX Crystal Guardians", 100),
    ("EX Dragon Frontiers", 101),
    ("EX Power Keepers", 108),
    ("Diamond & Pearl", 130),
    ("Mysterious Treasures", 124),
    ("Secret Wonders", 132),
    ("Great Encounters", 106),
    ("Majestic Dawn", 100),
    ("Legends Awakened", 146),
    ("Stormfront", 106),
    ("Platinum", 133),
    ("Rising Rivals", 120),
    ("Supreme Victors", 153),
    ("Arceus", 111),
    ("HeartGold & SoulSilver", 124),
    ("Unleashed", 96),
    ("Undaunted", 91),
    ("Triumphant", 103),
    ("Call of Legends", 106),
    ("Black & White", 115),
    ("Emerging Powers", 98),
    ("Noble Victories", 102),
    ("Next Destinies", 103),
    ("Dark Explorers", 111),
    ("Dragons Exalted", 128),
    ("Dragon Vault", 21), ## Special set.  (Gen. V)
    ("Boundaries Crossed", 153),
    ("Plasma Storm", 138),
    ("Plasma Freeze", 122),
    ("Plasma Blast", 105),
    ("Legendary Treasures", 140),
    ("Kalos Starter Set", 39), ## Special set.  (Gen. VI)
    ("XY", 146),
    ("Flashfire", 110),
    ("Furious Fists", 114),
    ("Phantom Forces", 124),
    ("Primal Clash", 164),
    ("Double Crisis", 34), ## Special set.  (Gen. VI)
    ("Roaring Skies", 112),
    ("Ancient Origins", 101),
    ("BREAKthrough", 165),
    ("BREAKpoint", 126),
    ("Generations", 117), ## Special set.  (Gen. VI)
    ("Fates Collide", 129),
    ("Steam Siege", 116),
    ("Evolutions", 113),
    ("Sun & Moon", 154),
    ("Guardians Rising", 180),
    ("Burning Shadows", 177),
    ("Shining Legends", 81), ## Special set.  (Gen. VII)
    ("Crimson Invasion", 126),
    ("Ultra Prism", 178),
    ("Forbidden Light", 150),
    ("Celestial Storm", 187),
    ("Dragon Majesty", 80), ## Special set.  (Gen. VII)
    ("Lost Thunder", 240),
    ("Team Up", 198),
    ("Dectective Pikachu", 18), ## Special set.  (Gen. VII)
    ("Unbroken Bonds", 238),
    ("Unified Minds", 261),
    ("Hidden Fates", 163), ## Special set.  (Gen. VII)
    ("Cosmic Eclipse", 272),
    ("Sword & Shield", 216),
    ("Rebel Clash", 209),
    ("Darkness Ablaze", 201),
    ("Champion's Path", 80), ## Special set.  (Gen. VIII)
    ("Vivid Voltage", 203),
    ("Shining Fates", 195), ## Special set.  (Gen. VIII)
    ("Battle Styles", 183),
    ("Chilling Reign", 233),
    ("Evolving Skies", 237),
    ("Celebrations", 50), ## Special set.  (Gen. VIII)
    ("Fusion Strike", 284),
    ("Brilliant Stars", 216),
    ("Astral Radiance", 246),
    ("Pokemon GO", 88), ## Special set.  (Gen. VIII)
    ("Lost Origin", 247),
    ("Silver Tempest", 245),
    ("Crown Zenith", 230), ## Special set.  (Gen. VIII)
    ("Scarlet & Violet", 258),
    ("Paldea Evolved", 279),
    ("Obsidian Flames", 230),
    ("Scarlet & Violet: 151", 207), ## Special set.  (Gen. IX)
    ("Paradox Rift", 266),
    ("Paldean Fates", 245), ## Special set.  (Gen. IX)
    ("Temporal Forces", 218),
    ("Twilight Masquerade", 226),
    ("Shrouded Fable", 99), ## Special set.  (Gen. IX)
    ("Surging Sparks", 252),
    ("Prismatic Evolutions", 180), ## Special set. (Gen. IX)
    ("Journey Together", 180),
]   #TODO: make a way to read sets at a 'glance' from a website
    #TODO: read from a website instead of manual entry

# initialize variables
binder_size_limit = 504
current_binder = []
binders = []

# iterate through the sets and group them into binders
for set_name, set_total in sets_data:
    if sum(current_binder) + set_total <= binder_size_limit:
        current_binder.append(set_total)
    else:
        # else start a new binder 
        binders.append(current_binder)
        current_binder = [set_total]

# add the last binder if it's not empty
if current_binder:
    binders.append(current_binder)

# print the binders and the sets contained within them
for i, binder in enumerate(binders):
    binder_total = sum(binder)
    print(f"Binder {i + 1} (Total: {binder_total}):")
    for j, set_total in enumerate(binder):
        print(f"{sets_data.pop(0)[0]} ({set_total} cards)")
    print()
