// ==========  This file is under  LGPL, the GNU Lesser General Public Licence
// ==========  Dialing Lemmatizer (www.aot.ru), 
// ==========  Copyright by Alexey Sokirko (2004)

// This source code is higly optimized (no std::vectors or std::fstream) 
// The load time of morphology dictionaries is important.

#include "MorphAutomat.h"

static int  InitAlphabet(MorphLanguageEnum Language, int* pCode2Alphabet, int *pAlphabet2Code, size_t AnnotChar)
{
	assert (!is_upper_alpha((BYTE)AnnotChar, Language));
	std::string AdditionalEnglishChars = "'1234567890";
	std::string AdditionalGermanChars = "";
	int AlphabetSize = 0;
	for (size_t i=0; i < 256; i++)
	{
		if	(		is_upper_alpha((BYTE)i, Language) 
				||	(i == '-') 
				||	(i == AnnotChar)
				||	(		(Language == morphEnglish) 
						&&	(AdditionalEnglishChars.find((BYTE)i) != std::string::npos)
					)
				||	(		(Language == morphGerman) 
						&&	(AdditionalGermanChars.find((BYTE)i) != std::string::npos)
					)
				||	(		(Language == morphURL) 
					  &&	is_alpha((BYTE)i, morphURL)
					 )
			)
		{
			pCode2Alphabet[AlphabetSize] = (int)i;
			pAlphabet2Code[i] = AlphabetSize;
			AlphabetSize++;
		}
		else
			pAlphabet2Code[i] = -1;

	};

	if (AlphabetSize > MaxAlphabetSize)
	{
		std::string Error = "Error! The  ABC is too large";
		ErrorMessage (Error);
		throw CExpc(Error);
	};

	return AlphabetSize;
};
std::string CABCEncoder::GetCriticalNounLetterPack() const
{
	return std::string(MinimalPredictionSuffix, m_AnnotChar);
}

std::string CABCEncoder::EncodeIntToAlphabet(uint32_t v) const
{
	std::string Result;
	if (v == 0)
	{
		Result.push_back(m_Code2AlphabetWithoutAnnotator[0]);
		const char* debug = Result.c_str();
		return Result;
	}
	else
	while (v > 0)
	{
		Result.push_back(m_Code2AlphabetWithoutAnnotator[v%m_AlphabetSizeWithoutAnnotator]);
		v  /= m_AlphabetSizeWithoutAnnotator;
	};
	return Result;
};

uint32_t CABCEncoder::DecodeFromAlphabet(const std::string& v) const
{
	size_t len = v.length();
	int c = 1;
	int Result = 0;
	for (size_t i=0; i <len; i++)
	{
		Result += m_Alphabet2CodeWithoutAnnotator[(BYTE)v[i]]*c;
		c*=m_AlphabetSizeWithoutAnnotator;
	};
	return Result;
};

void  CABCEncoder::CheckABCWithAnnotator(const std::string& WordForm) const
{
	for (size_t i = 0; i < WordForm.length(); i++)
		if (m_Alphabet2Code[(BYTE)WordForm[i]] == -1) {
			throw CExpc("Bad ABC Word=\"%s\", char='%c', index=%i", WordForm.c_str(), WordForm[i], i);
		}
};

bool  CABCEncoder::CheckABCWithoutAnnotator(const std::string& WordForm) const
{
	for (size_t i=0; i < WordForm.length(); i++)
		if (m_Alphabet2CodeWithoutAnnotator[(BYTE)WordForm[i]] == -1)
			return false;
	return true;
};


CABCEncoder::CABCEncoder(MorphLanguageEnum Language, BYTE AnnotChar) : m_AnnotChar(AnnotChar)
{
	m_AlphabetSize = ::InitAlphabet(Language,m_Code2Alphabet,m_Alphabet2Code,m_AnnotChar);
	m_AlphabetSizeWithoutAnnotator = ::InitAlphabet(Language,m_Code2AlphabetWithoutAnnotator,m_Alphabet2CodeWithoutAnnotator,257/* non-exeting symbol */);
	assert (m_AlphabetSizeWithoutAnnotator + 1 == m_AlphabetSize);
	m_Language = Language;
};



CMorphAutomat::CMorphAutomat(MorphLanguageEnum Language, BYTE AnnotChar) : CABCEncoder(Language, AnnotChar)
{
	m_pNodes = 0;
	m_pRelations = 0;
	m_NodesCount = 0;
	m_RelationsCount = 0;
};

CMorphAutomat::~CMorphAutomat()
{
	Clear();
};

void CMorphAutomat::Clear()
{
	if (m_pNodes)
		delete m_pNodes;
	m_pNodes = 0;
	m_NodesCount = 0;

	if (m_pRelations)
		delete m_pRelations;
	m_pRelations = 0;
	m_RelationsCount = 0;
};


void CMorphAutomat::BuildChildrenCache()
{
	size_t Count = ChildrenCacheSize;
	if (m_NodesCount < ChildrenCacheSize)
		Count = m_NodesCount;

	m_ChildrenCache.resize(Count*MaxAlphabetSize, -1);
	
	
	for (size_t NodeNo=0; NodeNo <Count; NodeNo++)
	{
		const CMorphAutomRelation* start = m_pRelations+m_pNodes[NodeNo].GetChildrenStart();
		const CMorphAutomRelation* end = start + GetChildrenCount(NodeNo);
		for (; start != end; start++)
		{
			const CMorphAutomRelation& p = *start;
			m_ChildrenCache[NodeNo*MaxAlphabetSize+m_Alphabet2Code[p.GetRelationalChar()]] = p.GetChildNo();
		};
	};
	
};

void CMorphAutomat::Load(std::string AutomatFileName)
{
	Clear();
	
	FILE * fp = fopen(AutomatFileName.c_str(), "rb");
	if (!fp)
	{
		throw CExpc(Format("Cannot open %s", AutomatFileName.c_str()));
	};
	
	char buffer [256];
	if (!fgets(buffer, 256, fp)) throw CExpc("cannt read nodes count");
	m_NodesCount = atoi(buffer);
	if (!m_NodesCount) throw CExpc(Format("nodes count cannot be 0 in %s", AutomatFileName.c_str()));

	assert (m_pNodes == 0);
	
	m_pNodes  = new CMorphAutomNode[m_NodesCount];
	assert (m_pNodes != 0);
	if (fread(m_pNodes, sizeof(CMorphAutomNode),m_NodesCount, fp) != m_NodesCount)
		throw CExpc(Format("Cannot read m_pNodes from %s", AutomatFileName.c_str()));;
	

	if (!fgets(buffer, 256, fp)) throw CExpc("cannot read relations count");
	m_RelationsCount = atoi(buffer);
	assert (m_pRelations == 0);
	m_pRelations  = new CMorphAutomRelation[m_RelationsCount];
	assert (m_pRelations != 0);
	if (fread(m_pRelations, sizeof(CMorphAutomRelation),m_RelationsCount, fp) != m_RelationsCount)
		throw CExpc(Format("Cannot read m_pRelations from %s", AutomatFileName.c_str()));;
	

	{
		int Alphabet2Code[256];
		if (fread(Alphabet2Code,sizeof(int),256,fp) != 256)  {
            throw CExpc(Format("Cannot read Alphabet2Code from %s", AutomatFileName.c_str()));;
        }
		if (memcmp(Alphabet2Code,m_Alphabet2Code, 256*sizeof(int)) )
		{
			std::string err = Format("%s alphabet has changed; cannot load morph automat", GetStringByLanguage(m_Language).c_str());
			throw CExpc(err);
		};
	};
	fclose(fp);
	BuildChildrenCache();
};

void CMorphAutomat::Save(std::string AutomatFileName) const
{
	FILE * fp = fopen(AutomatFileName.c_str(), "wb");
	if (!fp)
		throw CExpc(Format("cannot open file %s", AutomatFileName.c_str()));
	fprintf(fp, "%i\n", (int)m_NodesCount);
	if (fwrite(m_pNodes, sizeof(CMorphAutomNode), m_NodesCount, fp) != m_NodesCount) {
		fclose(fp);
		throw CExpc(Format("cannot write nodes to %s", AutomatFileName.c_str()));
	}

	fprintf(fp, "%i\n", (int)m_RelationsCount);
	if (fwrite(m_pRelations, sizeof(CMorphAutomRelation), m_RelationsCount, fp) != m_RelationsCount) {
		fclose(fp);
		throw CExpc(Format("cannot write relations to %s", AutomatFileName.c_str()));
	}
		
	fwrite(m_Alphabet2Code,sizeof(int),256,fp);
	fclose(fp);
	std::cout << m_RelationsCount << " children\n";
	std::cout << m_NodesCount << " nodes\n";
};


size_t  CMorphAutomat::GetChildrenCount(size_t NodeNo)  const
{  
	//return m_Nodes[NodeNo].m_ChildrenEndIndex - m_Nodes[NodeNo].m_ChildrenStartIndex;
	if (NodeNo+1 == m_NodesCount)
			return m_RelationsCount - m_pNodes[NodeNo].GetChildrenStart();
	else
			return m_pNodes[NodeNo+1].GetChildrenStart() - m_pNodes[NodeNo].GetChildrenStart();

};


const CMorphAutomRelation*  CMorphAutomat::GetChildren(size_t NodeNo) const 
{ 
	return m_pRelations + m_pNodes[NodeNo].GetChildrenStart(); 
};



void CMorphAutomat::DumpAllStringsRecursive(FILE* fp, int NodeNo, std::string CurrPath) const 
{
	if (m_pNodes[NodeNo].IsFinal())
	{
		fprintf (fp, "%s\n", CurrPath.c_str());
	};
	size_t Count =  GetChildrenCount(NodeNo);
	for (size_t i=0; i<Count; i++)
	{
		const CMorphAutomRelation& p = GetChildren(NodeNo)[i];
		std::string q = CurrPath;
		q.push_back(p.GetRelationalChar());
		DumpAllStringsRecursive(fp, p.GetChildNo(), q);
	};

};

bool CMorphAutomat::DumpAllStrings(std::string FileName) const 
{
	FILE *fp  = fopen (FileName.c_str(), "w");
	if (!fp) return false;
	if (m_NodesCount > 0 ) 
		DumpAllStringsRecursive(fp, 0, "");
	fclose (fp);
	return true;
};



int CMorphAutomat::NextNode(int NodeNo, BYTE RelationChar) const
{
	if (NodeNo < ChildrenCacheSize)
	{
		int z = m_Alphabet2Code[RelationChar];
		if (z == -1) return -1;
		return m_ChildrenCache[NodeNo*MaxAlphabetSize+z];
	}
	else
	{
		const CMorphAutomRelation* start = m_pRelations +m_pNodes[NodeNo].GetChildrenStart();
		const CMorphAutomRelation* end = start + GetChildrenCount(NodeNo);

		for (; start != end; start++)
		{
			const CMorphAutomRelation& p = *start;
			if (RelationChar == p.GetRelationalChar())
				return p.GetChildNo();
		};

		return -1;
	};
};


std::string	CMorphAutomat::GetFirstResult (const std::string& Text) const 
{
	int NodeNo = FindStringAndPassAnnotChar(Text, 0);
	if ( NodeNo == -1) return "";
	std::string res = "";
	while (!m_pNodes[NodeNo].IsFinal())
	{
		const CMorphAutomRelation& p = GetChildren(NodeNo)[0];
		res.push_back(p.GetRelationalChar());
		NodeNo = p.GetChildNo();
	};
	return res;
};

void	CMorphAutomat::GetAllMorphInterpsRecursive (int NodeNo, std::string& curr_path, std::vector<CAutomAnnotationInner>& Infos) const 
{
	const CMorphAutomNode& N = m_pNodes[NodeNo];
	if (N.IsFinal())
	{
		CAutomAnnotationInner A;
		uint32_t i = DecodeFromAlphabet(curr_path);
		size_t ItemNo;
		size_t ModelNo;
		size_t PrefixNo;
		DecodeMorphAutomatInfo(i, ModelNo, ItemNo, PrefixNo);
		A.m_ItemNo = (uint16_t)ItemNo;
		A.m_ModelNo = (uint16_t)ModelNo;
		A.m_PrefixNo = (uint16_t)PrefixNo;
		Infos.push_back(A);
	};

	size_t Count =  GetChildrenCount(NodeNo);
	size_t CurrPathSize = curr_path.size();
	curr_path.resize(CurrPathSize + 1);
	for (size_t i=0; i<Count; i++)
	{
		const CMorphAutomRelation& p = GetChildren(NodeNo)[i];
		curr_path[CurrPathSize] = p.GetRelationalChar();
		GetAllMorphInterpsRecursive(p.GetChildNo(), curr_path, Infos);
	};
	curr_path.resize(CurrPathSize);
};

int	CMorphAutomat::FindStringAndPassAnnotChar (const std::string& Text, size_t TextPos) const 
{
	size_t TextLength = Text.length();
	int r = 0;
	for (size_t i=TextPos; i<TextLength; i++)
	{
		int nd =  NextNode(r,(BYTE)Text[i]);
		
		if (nd ==  -1) 
		{
			return -1;		
		}
		r = nd;
	};
	//assert ( r != -1);
	//  passing annotation char

	return NextNode(r,m_AnnotChar);
};

void	CMorphAutomat::GetInnerMorphInfos (const std::string& Text, size_t TextPos, std::vector<CAutomAnnotationInner>& Infos) const 
{
	Infos.clear();
	int r = FindStringAndPassAnnotChar(Text, TextPos);
	if ( r == -1) return;

	// getting all interpretations
	std::string curr_path;
	GetAllMorphInterpsRecursive(r, curr_path, Infos);

	//assert (!Infos.empty());
	//sort(Infos.begin(),Infos.end());
};

uint32_t CMorphAutomat::EncodeMorphAutomatInfo (size_t ModelNo, size_t ItemNo, size_t PrefixNo) const 
{
	return			(((uint32_t)((uint16_t)((uint32_t)(ModelNo) & 0xffff))) << 18)
				|	(((uint32_t)((uint16_t)((uint32_t)(ItemNo) & 0xffff))) << 9)
				|	PrefixNo;

};

void CMorphAutomat::DecodeMorphAutomatInfo (uint32_t Info, size_t& ModelNo, size_t& ItemNo, size_t& PrefixNo) const 
{
	ModelNo = Info >>18;
	ItemNo  = (0x3FFFF&Info) >>9;
	PrefixNo = (0x1FF&Info);
};

