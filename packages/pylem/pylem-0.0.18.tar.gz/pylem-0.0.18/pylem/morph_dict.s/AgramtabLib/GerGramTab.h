// ==========  This file is under  LGPL, the GNU Lesser General Public Licence
// ==========  Dialing Lemmatizer (www.aot.ru)
// ==========  Copyright by Alexey Sokirko

#pragma once 

#include "agramtab_.h"       
#include "ger_consts.h"

class CGerGramTab : public CAgramtab
{
	const static size_t gStartUp = 0x4141; //AA 
	const static size_t gEndUp = 0x7A7B;  //zz + 1
	const static size_t gMaxGrmCount = gEndUp - gStartUp; // // 5911  (5 Кб) 
public:
	CAgramtabLine*  Lines[gMaxGrmCount];
	CGerGramTab();
	~CGerGramTab();

	part_of_speech_t GetPartOfSpeechesCount() const;
	const char* GetPartOfSpeechStr(part_of_speech_t i) const;
	grammem_t GetGrammemsCount()  const;
	const char* GetGrammemStr(size_t i) const;
	size_t GetMaxGrmCount() const;
	CAgramtabLine*& GetLine(size_t LineNo) { return Lines[LineNo]; }
	const CAgramtabLine* GetLine(size_t LineNo) const {return Lines[LineNo];}
	size_t GramcodeToLineIndex(const char * s ) const { return  (unsigned char) s[0]*0x100+(unsigned char) s[1] - gStartUp;};

	std::string LineIndexToGramcode(uint16_t i) const
	{ 
		i += gStartUp;
		char res[3];

		res[0] = (i >> 8);
		res[1] = (0xFF & i);
		res[2] = 0;
		return  res;
	};
	int GetGroupTypebyName(const char* TypeName) const;
	const char* GetRegistryString() const 
	{
		return "Software\\Dialing\\Lemmatizer\\German\\Ggramtab";
	};
	long GetClauseTypeByName(const char* TypeName) const;
	const char* GetClauseNameByType(long type) const;
	bool GleicheGenderNumber(const char* gram_code1, const char* gram_code2) const;
	bool GleicheSubjectPredicate(const char* gram_code1, const char* gram_code2) const;
	const size_t GetClauseTypesCount() const;
	bool IsStrongClauseRoot(const part_of_speech_mask_t poses) const;
	bool is_month (const char* lemma) const;
	bool is_small_number (const char* lemma) const;
	bool IsMorphNoun (part_of_speech_mask_t poses)  const;
	bool is_morph_adj (part_of_speech_mask_t poses) const;
	bool is_morph_participle (part_of_speech_mask_t poses) const;
	bool is_morph_pronoun (part_of_speech_mask_t poses) const;
	bool is_morph_pronoun_adjective(part_of_speech_mask_t poses) const;
	bool is_left_noun_modifier  (part_of_speech_mask_t poses, grammems_mask_t grammems) const;
	bool is_numeral (part_of_speech_mask_t poses) const;
	bool is_verb_form (part_of_speech_mask_t poses) const;
	bool is_infinitive(part_of_speech_mask_t poses) const;
	bool is_morph_predk(part_of_speech_mask_t poses) const;
	bool is_morph_adv(part_of_speech_mask_t poses) const;
	bool is_morph_personal_pronoun (part_of_speech_mask_t poses, grammems_mask_t grammems) const;
	bool is_morph_article(part_of_speech_mask_t poses) const;

	bool IsSimpleParticle(const char* lemma, part_of_speech_mask_t poses) const;
	bool IsSynNoun(part_of_speech_mask_t poses, const char* Lemma) const;
	bool IsStandardParamAbbr (const char* WordStrUpper) const;
	bool GleicheCase(const char* gram_code_noun, const char* gram_code_adj) const;
	bool GleicheCaseNumber(const char* gram_code1, const char* gram_code2) const;
	grammems_mask_t GleicheGenderNumberCase(const char* common_gram_code_noun, const char* gram_code_noun, const char* gram_code_adj) const;
	
};

const grammems_mask_t gAllCases = (_QM(gNominativ) | _QM(gGenitiv) | _QM(gDativ) | _QM(gAkkusativ));
const grammems_mask_t gAllNumbers = (_QM(gPlural) | _QM(gSingular));
const grammems_mask_t gAllGenders = (_QM(gFeminin) | _QM(gMaskulin) | _QM(gNeutrum));
const grammems_mask_t gAllPersons = (_QM(gErstePerson) | _QM(gZweitePerson) | _QM(gDrittePerson));
const grammems_mask_t gAllVerbForms = (_QM(gKonj1) | _QM(gKonj2) | _QM(gImperativ) | _QM(gPrasens) | _QM(gPraeteritum));
const grammems_mask_t gAllVerbClasses = (_QM(gModal) | _QM(gAuxiliar) | _QM(gSchwach) | _QM(gNichtSchwach));

