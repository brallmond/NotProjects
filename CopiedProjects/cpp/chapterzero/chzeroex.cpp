#include <iostream>

int main()
{
	int add;
	add = 3+4;

	std::cout << "Ex 0.1" << std::endl;
	std::cout << add << std::endl;

	std::cout << "Ex 0.2" << std::endl;
	std::cout << "This (\") is a quote, and this (\\) is a backslash" << std::endl;
	
	std::cout << "Ex 0.3" << std::endl;
	std::cout << "tab?" << "\t" << "tab??" << std::endl;

	std::cout << "Ex 0.4" << std::endl;
	std::cout << "// a small C++ program" << "\n" << "#include <iostream>" << "\n" << "\n" << "int main()" << "{" << "\n" << "\t" << "std::cout << \" Hello, world! \" << std::endl;" << "\n" << "\t" << "return 0;" << "\n" << "}"<< std::endl;

	std::cout << "Ex 0.5" << std::endl;
	std::cout << "ex 5 not a valid program. missing curly braces" << std::endl;

	std::cout << "Ex 0.6" << std::endl;
	{std::cout << "if this works then ex 6 is a valid program" << std::endl;}

	std::cout << "Ex 0.7" << std::endl;
	std::cout << "ex 7 is a valid program" << std::endl;

	std::cout << "Ex 0.8" << std::endl;
	std::cout << "ex 8 is a valid program" << std::endl;

	std::cout << "Ex 0.9" << std::endl;
	std::cout << "The shortest valid program is a null statement, right?" << std::endl;

	std::cout << "Ex 0.10" << std::endl;
	std::cout << "Rewrite helloworld so all white space is replaced with a newline" << std::endl;
	std::cout << "I answered this by removing all the white space I could in the original program and putting newlines where I couldn't" << std::endl;

	return 0;
}
