#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <vector>

using std::vector;

int main()
{
	// tell the user what you're gonna do
	std::cout << "I'll separate into quartiles the data"
		" that you give me. Please give me at least"
	       " eight data points followed by end-of-file."
	       << std::endl;

	// make a vector and store data in it
	vector<double> data;
	double x;
	while(std::cin >> x)
		data.push_back(x);

	// make sure the user gave you enough data
	typedef vector<double>::size_type vec_size;
	vec_size size = data.size();
	if (size < 4){ std::cout << "I need at least 4 data points. "
		"Please try again." << std::endl; return 1;}

	// sort data in 'non-decreasing' order
	sort(data.begin(), data.end());

	// find first quartile (lowest quarter of data)
	int onequart;
	onequart = size % 4 == 0 ? size/4 : size/4 + 1;
	
	for(int i = 0; i != size; ++i)
	{
		if(i == onequart || i == 2*onequart || i == 3*onequart){std::cout << "| " << data[i] << " ";}
		else{std::cout << data[i] << " ";}
	}

	return 0;
}
