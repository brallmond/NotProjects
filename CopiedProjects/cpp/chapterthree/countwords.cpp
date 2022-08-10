#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using std::string;	using std::vector;
using namespace std;
int main()
{
	cout << "I'll tell you how many times you say each word in"
		" a sentence that you type into me, separated by enters. "
		"I'll also tell you how long your longest and shortest "
		"words are. Please end input with end-of-file." << endl;

	vector<string> input;
	vector<int> wordlen;
	string word;
	while(cin >> word)
	{
		input.push_back(word);
		wordlen.push_back(word.size());
	}

	vector<string> repeatedwords;
	vector<string> unrepeatedwords;
	vector<int> itswordcount;
	for(int i = 0; i != input.size(); ++i)
	{
		int wordcount = 0;
		string cword = input[i];

		for(int j = 0; j != input.size(); ++j)
		{
			if(cword == input[j]){wordcount+=1;}
		}
		if(wordcount > 1)
		{
			repeatedwords.push_back(cword);
			itswordcount.push_back(wordcount);
		}
		else{unrepeatedwords.push_back(cword);}
	}
	cout << "These are words you said just once: " << endl;
	for(int j = 0; j != unrepeatedwords.size(); ++j)
	{
		cout << "\"" << unrepeatedwords[j] << "\", ";
	}
	vector<string> printedreps;
	cout << "and these are words you said more than once: " << endl;
	for(int j = 0; j != repeatedwords.size(); ++j)
	{
		bool print = true;
		string nword = repeatedwords[j];
		int ncount = itswordcount[j];
		for(int k = 0; k != printedreps.size(); ++k)
		{
			if(nword == printedreps[k]){print = false;}
		}
		if(print == true)
		{
			cout << "\"" << nword << "\" " << ncount << " times" << endl;
		}
		printedreps.push_back(repeatedwords[j]);
	}

	sort(wordlen.begin(),wordlen.end());

	int maxlen = wordlen[wordlen.size() - 1];
	int minlen = wordlen[0];

	cout << endl << "The longest word you entered was " << maxlen << " characters long." << endl;
	cout << endl << "The shortest word you entered was " << minlen << " characters long." << endl;
	return 0;
}
