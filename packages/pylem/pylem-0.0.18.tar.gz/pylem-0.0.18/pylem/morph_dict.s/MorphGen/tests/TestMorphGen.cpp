#include "morph_dict/LemmatizerBaseLib/MorphanHolder.h"
#include <fstream>
#include <streambuf>

int Lemmatize(MorphLanguageEnum langua, std::string folder, std::string word, std::string canon_file) {
    CMorphanHolder Holder;
    Holder.LoadLemmatizer(langua, folder);
    word = convert_from_utf8(word.c_str(), Holder.m_CurrentLanguage);
    std::ofstream outp("test_word.morph", std::ios::binary);
    std::string test = Holder.PrintMorphInfoUtf8(word, false, false, true) + "\n";
    outp << test.c_str();
    outp.close();

    std::ifstream canon_fp(canon_file);
    std::string canon((std::istreambuf_iterator<char>(canon_fp)),
        std::istreambuf_iterator<char>());
    return canon == test;
}

int main(int argc, const char* argv[])
{
    if (argc != 4) {
        std::cerr << "usage: TestMorphGen <folder> <word> <canon_file>";
        return 1;
    }
    try {
        std::string folder = argv[1];
        std::string word = argv[2];
        std::string canon_file = argv[3];
        auto res = Lemmatize(morphRussian, folder, word, canon_file) ? 0 : 1;
        std::cerr << "res=" << res << "\n";
        return res;
    }
    catch (CExpc c) {
        std::cerr << c.m_strCause << "\n";
        return 1;
    }
    catch (...) {
        std::cerr << "general exception\n";
        return 1;
    }
}
