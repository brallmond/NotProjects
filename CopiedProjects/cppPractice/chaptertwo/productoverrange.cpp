#include <iostream>

int main()
{
	std::cout << "I'll find the product of the range you input where the end number is not inclusive. [Start, End)" << std::endl;
	std::cout << "Start range? " << std::endl;

	int start;
	std::cin >> start;

	std::cout << "End range? " << std::endl;

	int end;
	std::cin >> end;

	int productoverrange = 1;
	for(int i = 0; start+i != end; ++i)
	{
		productoverrange *= (start + i);
	}

	std::cout << "The product over the given range is " << productoverrange << std::endl;

	return 0;
}
