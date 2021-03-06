from nltk.stem import SnowballStemmer
from nltk.stem.api import StemmerI
import nltk
import json

class ParticleStemmer(SnowballStemmer):

	def __init__(self, language="english", ignore_stopwords=False, suffix_rule_list={}):
		super().__init__(language=language, ignore_stopwords=ignore_stopwords)
		if language == "english":
			self.stemmer._EnglishStemmer__special_words.update({
				"experiment":"experiment", 
				"experimented":"experiment", 
				"experimenting":"experiment", 
				"experiments":"experiment",
				'organization': 'organiz',
				"organization's": 'organiz',
				'organizational': 'organiz',
				'organizationally': 'organiz',
				'organizations': 'organiz',
				'organize': 'organiz',
				'organized': 'organiz',
				'organizer': 'organiz',
				'organizers': 'organiz',
				'organizes': 'organiz',
				'organizing': 'organiz',
				'science': 'scient',
				'sciences': 'scient',
				'scientific': 'scient',
				'scientifically': 'scient',
				'scientist': 'scient',
				'scientistic': 'scient',
				'scientists': 'scient',
				'animal': 'animal',
				'animalism': 'animal',
				'animalistic': 'animal',
				'animalities': 'animal',
				'animality': 'animal',
				'animals': 'animal',
				'customer': 'customer',
				'ratability': 'rate',
				'ratable': 'rate',
				'ratably': 'rate',
				'rate': 'rate',
				'rateable': 'rate',
				'rateably': 'rate',
				'rated': 'rate',
				'rater': 'rate',
				'raters': 'rate',
				'rates': 'rate',
				'rating': 'rate',
				'ratings': 'rate',
				'ratio': 'rate',
				'ratios': 'rate',
				'ration': 'ration',
				'rations': 'ration',
				'rationed': 'ration',
				'rationing': 'ration',
				'ratification': 'ratifi',
				'ratified': 'ratifi',
				'ratifier': 'ratifi',
				'ratifiers': 'ratifi',
				'ratifies': 'ratifi',
				'ratify': 'ratifi',
				'ratifying': 'ratifi',
				'rational': 'rational',
				'rationale': 'rational',
				'rationales': 'rational',
				'rationalism': 'rational',
				'rationalist': 'rational',
				'rationalistic': 'rational',
				'rationalistically': 'rational',
				'rationalists': 'rational',
				'rationalities': 'rational',
				'rationality': 'rational',
				'rationalization': 'rational',
				'rationalizations': 'rational',
				'rationalize': 'rational',
				'rationalized': 'rational',
				'rationalizer': 'rational',
				'rationalizers': 'rational',
				'rationalizes': 'rational',
				'rationalizing': 'rational',
				'rationally': 'rational',
				'rationalness': 'rational',
				'rationals': 'rational',
				'ionization': 'ion',
				'ionizer': 'ion',
				'ionizers': 'ion',
				'ionizations': 'ion',
				'chemistry': 'chem', 
				'chemistries': 'chem', 
				'chemist': 'chem',
				'chemists': 'chem',
				'chemism': 'chem',
				'chemisms': 'chem',
				'stable': 'stabil',
				'stabled': 'stabil',
				'stableness': 'stabil', 
				'laboratorial': 'lab',
				'laboratorially': 'lab',
				'laboratorian': 'lab',
				'laboratories': 'lab',
				'laboratory': 'lab',
				'preppie': 'prep',
				'preppies': 'prep',
				'preparation': 'prep',
				'preparations': 'prep',
				'preparatorily': 'prep',
				'preparatory': 'prep',
				'prepare': 'prep',
				'prepared': 'prep',
				'preparedness': 'prep',
				'preparer': 'prep',
				'preparers': 'prep',
				'prepares': 'prep',
				'preparing': 'prep',
				'publication': 'publish',
				'publications': 'publish',
				'microfluidiсs': 'microfluid', 
				'microfluidiс': 'microfluid', 
				'transmissibility': 'transmitt',
				'transmissible': 'transmitt',
				'transmission': 'transmitt',
				'transmissions': 'transmitt',
				'transmissive': 'transmitt',
				'transmitting': 'transmitt',
				'transmitted': 'transmitt',
				'transmit': 'transmitt',
				'transmits': 'transmitt',
				'compliant': 'complianc',
				'compliantly': 'complianc',
				'allergic': 'allergen',
				'allergies': 'allergen',
				'allergin': 'allergen',
				'allergist': 'allergen',
				'allergists': 'allergen',
				'allergology': 'allergen',
				'allergy': 'allergen',
				'reproduction': 'reproduc',
				'reproductions': 'reproduc',
				'reproductive': 'reproduc',
				'reproductively': 'reproduc',
				'reproductiveness': 'reproduc',
				'reproductivity': 'reproduc',
				'filtrable': 'filter',
				'filtrate': 'filter',
				'filtrated': 'filter',
				'filtrates': 'filter',
				'filtrating': 'filter',
				'filtration': 'filter',
				'programmable': 'program',
				'programmability': 'program',
				'programme': 'program', 
				'programmata': 'program', 
				'programmatic': 'program', 
				'programmatically': 'program', 
				'programmer': 'program',
				'programmers': 'program',
				'programmes': 'program',
				'formation': 'form',
				'include': 'inclus',
				'includes': 'inclus',
				'including': 'inclus',
				'included': 'inclus',
				'dosage': 'dose',
				'dosages': 'dose',
				'seq':'sequenc',
				'mineral':'mineral',
				'minerals':'mineral',
				'mineralization':'mineral',
				'mineralize':'mineral',
				'mineralized':'mineral',
				'mineralizes':'mineral',
				'mineralizing':'mineral',
				'designate':'designat',
				'designated':'designat',
				'designates':'designat',
				'designating':'designat',
				'designation':'designat',
				'designations':'designat',
				'designative':'designat',
				'designator':'designat',
				'designment':'designat',
				'genesys':'genesys',
				'poly':'poly',
				'sepsis':'sept',
				'fabulist':'fabl',
				'fabulists':'fabl',
				'flautist':'flut',
				'flautists':'flut',
				'hygeist':'hygien',
				'hygieist':'hygien',
				'hygeists':'hygien',
				'hygieists':'hygien',
				'hypothesist':'hypothe',
				'hypothesists':'hypothe',
				'lutanist':'lute',
				'lutanists':'lute',
				'lutenist':'lute',
				'lutenists':'lute',
				'lutist':'lute',
				'lutists':'lute',
				'magisterial':'magist',
				'magisterially':'magist',
				'magisterialness':'magist',
				'magistery':'magist',
				'magistracies':'magist',
				'magistracy':'magist',
				'magistrateship':'magist',
				'magistrature':'magist',
				'mister':'mister',
				'mr':'mister',
				'misters':'mister',
				'mistier':'misti',
				'mistiest':'misti',
				'piano':'pian',
				'pianos':'pian',
				'cellist':'cello',
				'cellists':'cello',
				'orthopaedic':'orthoped',
				'orthopaedics':'orthoped',
				'orthopaedist':'orthoped',
				'orthopaedist':'orthoped',
				'papist':'papa',
				'papistries':'papa',
				'papistry':'papa',
				'papists':'papa',
				'protista':'protist',
				'rapist':'rape',
				'rapists':'rape',
				'scenarist':'scenario',
				'scenarists':'scenario',
				'tourism':'tourist',
				'tourisms':'tourist',
				'admin':'administr',
				'administer':'administr',
				'administered':'administr',
				'administerial':'administr',
				'administering':'administr',
				'administerings':'administr',
				'administers':'administr',
				'administratrices':'administr',
				'administratrix':'administr',
				'characterless':'charact',
				'charactery':'charact',
				'geoscience': 'geoscient',
				'geosciences': 'geoscient',
				'geoscientific': 'geoscient',
				'geoscientifically': 'geoscient',
				'geoscientist': 'geoscient',
				'geoscientistic': 'geoscient',
				'geoscientists': 'geoscient',
				'bioscience': 'bioscient',
				'biosciences': 'bioscient',
				'bioscientific': 'bioscient',
				'bioscientifically': 'bioscient',
				'bioscientist': 'bioscient',
				'bioscientistic': 'bioscient',
				'bioscientists': 'bioscient',
				})
			
			from partstem.word_list import word_list
			self.word_list = word_list
			self.word_list += nltk.corpus.words.words()
			
			self.stem = self.__stem
			self.suffix_rule_list = {
				'ant': {"with": ['ation'], "exception": []},
				'eti': {"with": ['ant', ''], "exception": []},
				'or': {"with": ['ion'], "exception": []},
				'um': {"with": ['a'], "exception": ["medium"]},
				'a': {"with": ['um', 'ary+ '], "exception": ["media"]},
				'ri': {"with": [' -ried', 'er', 'tes'], "exception": []},
				'er': {"with": ['y'], "exception": []},
				'al': {"with": ['us'], "exception": ["animal"]},
				'us': {"with": ['al'], "exception": []},
				'ifi': {"with": ['e'], "exception": ["modifi", "specifi"]},
				'e': {"with": ['ification'], "exception": []},
				'ion': {"with": ['e'], "exception": []},
				'i': {"with": ['e', 'us', 'er', 'y+ ', 'y+ic'], "exception": ["ii"]},
				'si': {"with": ['sis'], "exception": ["genesi"]},
				's': {"with": ['sis'], "exception": ["genes"]},
				't': {"with": ['sis'], "exception": []},
				'z': {"with": ['sis'], "exception": []},
				"ier": {"with": ["ying", ""], "exception": []},
				"abl": {"with": ["e", "es", "ate", "ation", "ed", "en", "ies", ""], "exception": ["stabl", "capabl", "fabl", "arabl", "cabl", "constabl", "decasyllabl", "despicabl", "diabl", "disabl", "effabl", "enabl", "formidabl", "gabl", "gullabl", "impeccabl", "improbabl", "incapabl", "ineffabl", "inevitabl", "inviabl", "invariabl", "viabl", "variabl", "liabl", "probabl", "syllabl", "monosyllabl", "nonstabl", "unstabl", "uncapabl", "nonviabl", "parabl", "peccabl", "polysyllabl", "sabl", "permeabl", "semipermeabl", "tabl", "tenabl", "thermostabl", "timetabl", "unabl", "vegetabl", "vocabl", "worktabl"]}, 
				"th": {"with": [""], "exception": []},
				"atori": {"with": ["ation"], "exception": []},
				"ori": {"with": ["ion"], "exception": []},
				"ous": {"with": ["y", "", "e", "on", "ity"], "exception": []},
				"ic": {"with": ["", "e"], "exception": ["sonic", "polic", "indic"]},
				"iti": {"with": ["est+ification"], "exception": []},
				"iz": {"with": ["ize", "izate"], "exception": []},
				"at": {"with": ["atic", "ance"], "exception": []},
				'if': {"with": ["ity+est", "e"], "exception": ["modif", "specif"]},
				'ist': {"with": ['ism', 'ed', 'ical', 'y', 'ium', 'est', 'ic', 'e', 'o', 'al', 'a', ''], "exception": ["mist", "agonist", "assist", "list", "backlist", "ballist", "banist", "bannist", "barrist", "batist", "booklist", "canist", "casuist", "checklist", "christ", "cist", "fist", "closefist", "exist", "coexist", "consist", "delist", "desist", "enlist", "twist", "entwist", "feist", "filist", "foist", "gist", "grist","hagadist", "heist", "heurist", "hist", "hoist", "inconist", "insist", "intwist", "resist", "irresist", "joist", "kist", "legist", "logist", "magist", "maist", "minist", "modist", "moist", "specialist", "sophist", "statist", "waist", "pantywaist", "persist", "poltergeist", "preenlist", "preexist", "regist", "protist", "reenlist", "relist", "shirtwaist", "shist", "sinist", "subsist", "tourist", "underwaist", "unlist", "untwist", "whist", "wist", "wrist", "zeitgeist"]},
				'ism': {"with": ['ist', 'ic', ''], "exception": ["tourism"]},
			}
			self.suffix_rule_list.update(suffix_rule_list)
			self.suffix_list = sorted(list(self.suffix_rule_list.keys()), key=lambda x: -len(x))

	def __stem(self, word, return_snowball=False):
		if not word.startswith("improv"):
			remove_suffix = {"isate":"izate", "isated":"izated", "isating":"izating", "isates":"izates"}
			for key in remove_suffix.keys():
				if word.endswith(key):
					word = word[:-len(key)] + remove_suffix[key]
					break

			remove_suffix = {"ise":"ize", "ised":"ized", "ising":"izing", "ises":"izes"}
			for key in remove_suffix.keys():
				if word.endswith(key):
					new_word = word[:-len(key)] + remove_suffix[key]
					if new_word in self.word_list:
						word = new_word
						break
		
		word = self.stemmer.stem(word)
		stem_word = word
		num = 0
		if word not in list(self.stemmer._EnglishStemmer__special_words.keys()) + list(self.stemmer._EnglishStemmer__special_words.values()) and len(word) >= 3:
			while num < len(self.suffix_list):
				if stem_word.endswith(self.suffix_list[num]) and stem_word not in self.suffix_rule_list[self.suffix_list[num]]["exception"]:
					without_suffix = stem_word[:-len(self.suffix_list[num])]
					if len(without_suffix) == 0:
						num += 1
						continue
					for el in self.suffix_rule_list[self.suffix_list[num]]["with"]:

						el = el.replace("+", " ")
						el = el.replace("-", " -") if "-" in el and " -" not in el else el
						el = el.split(" ")
						key = True
						for el1 in el:
							if not ((without_suffix + el1 in self.word_list and not el1.startswith("-")) or (without_suffix + el1.replace("-", "") not in self.word_list and el1.startswith("-"))):
								key = False
								break
						if key:
							stem_word = without_suffix
							break
					break
				num += 1

		return (stem_word, word) if return_snowball else stem_word if len(stem_word) >= 3 else word

partstem = ParticleStemmer()
			