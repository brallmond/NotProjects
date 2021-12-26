#include <iostream>
#include <string>
#include <locale> //std::tolower so all strings can be converted to lowercase

int main()
{
	std::string star = "*";

	//get shape
	std::cout << "What shape would you like? ";

	//read shape and convert to lowercase
	std::string shape;
	std::cin >> shape;
	std::string shape_low = "";
	for(int i = 0; i != shape.length(); ++i){
		shape_low += std::tolower(shape[i]);
	}
	shape = shape_low;

	if(shape == "triangle" || shape == "eqtriangle" || shape == "square" || shape == "rectangle")
	{
		if(shape == "square" || shape == "eqtriangle")
		{
			int base = 1;
			std::cout << "What's the length of the base?" << std::endl;
			std::cin >> base;

			std::cout << std::endl;

			if(shape == "square")
			{
				std::string starline(base, '*');
				for(int i = 0; i != base; ++i)
				{
					std::cout << starline << std::endl;
				}
			}
			else
			{
				for(int i = 0; i != base; ++i)
				{
					std::string sidespaces(base-i, ' ');
					std::string midstars(1+i, '*');
					std::string line = sidespaces + midstars;

					std::cout << line << std::endl;
				}
			}
		}
		else
		{ 
			int height;
			std::cout << "How tall? (1,2,3,4,...) " << std::endl;
			std::cin >> height;

			int width;
			std::cout << "How wide? (1,2,3,4,...) " << std::endl;
			std::cin >> width;

			if(shape == "rectangle")
			{
				std::string starline(width, '*');
				for(int i = 0; i != height; ++i)
				{
					std::cout << starline << std::endl;
				}
			}
			else
			{
				//it's not really possibly to make an arbitrary user input triangle
				//e.g. base 10, height 2 makes no sense. this function just produces right triangles
				//with equal height and base
				for(int i = 0; i != height; ++i)
				{
					std::string sidespaces(width-i, ' ');
					std::string midstars(1+i, '*');
					std::string line = sidespaces + midstars + sidespaces;

					std::cout << line << std::endl;
				}
			}
		}
	}

	else{std::cout << "Hmm, I don't know that shape" << std::endl;}

	return 0;
}
