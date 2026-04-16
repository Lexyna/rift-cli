from uuid import uuid4
import random

planetnames = ["Achilles", "Actaeon", "Autonoë", "Aeëtes", "Arcas", "Augeas", "Bellerophon", "Ceyx", "Codrus", "Epaphus", "Harmonia", "Hippolyta", "Iasion", "Ion", "Orion",
									"Pasiphae", "Helios", "Crete", "Perseus", "Phaeton", "Pyrrah", "Sciron", "Tityos", "Zethes", "Xylles", "Apis", "Bacchus", "Turnus", "Zulu", "Tahkar", "Mayari",
									"Tala", "Laon", "Oryol", "Astika", "Nakula", "Sita", "Vali", "Iravan", "Drona", "Bhima", "Sleipnir", "Fráech", "Kintarō", "Nezha", "Borr", "Dagur", "Eir", "Ēostre",
									"Frigg", "Fulla", "Rán", "Tyra", "Zel", "Terra", "Artio", "Bormana", "Carvonia", "Icanuna", "Lerina", "Nemetona", "Ritona", "Sirona", "Sulis", "Inciona", "Epona",
									"Erecura", "Tamesis", "Verbeia", "Vesunna", "Niskus", "Sucellus", "Losa", "Coruae", "Deiba", "Toga", "Ermae", "Picio", "Coruga", "Lugus", "Anu", "Grian", "Lí Ban",
									"Medb", "Danand", "Balor", "Miach", "Tuirenn", "Olwen", "Pwyll", "Mabon", "Llŷr", "Efnysien",
                                    "Antila", "Apus", "Aquarius", "Aquila", "Aries", "Ara", "Auriga", "Boötes", "Cealum", "Camelopardialis", "Cancer",
										 "Canes Venatici", "Canis Major", "Canis Minor", "Carina", "Cassiopeida", "Centaurus", "Cepheus", "Cetus", "Chamaeleon", "Columba",
										 "Coma Bereneices", "Corona Australis", "Corona Borealis", "Corvus", "Crater", "Crux", "Cygnus", "Delphinus", "Dorado", "Equuleus",
										 "Eridanus", "Fornax", "Gemini", "Grus", "Hercules", "Horologium", "Hydra", "Indus", "Lacreta", "Leo", "Leo Minor", "Lepus", "Libra",
										 "Lupus", "Lynx", "Lyra", "Mensa", "Micriscopium", "Monoceros", "Musca", "Norma", "Octans", "Ophiuchus", "Orion", "Pavo", "Pegasus",
										 "Perseus", "Pictor", "Pisces", "Pisces Austrinus", "Puppis", "Pyxis", "Sagitta", "Sagittarius", "Scporpius", "Sculptor", "Scutum",
										 "Serpens", "Sextan", "Taurus", "Telescopium", "Triangulum", "Triangulum Australe", "Tucana", "Ursa Major", "Ursa Minor", "Vela",
										 "Virgo", "Volans", "Vulpecula" ];

greekLetters = [ "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "my", "ny", "xi", "omnicron", "rho", "sigma", "tau", "upsilon", "chi", "psi", "omega" ];

def generate_planet_name() -> str:
    
    name = random.choice(planetnames)

    prefix = random.choice(greekLetters)

    return f"{prefix}-{name}"

def generate_id() -> str:
    return str(uuid4())
