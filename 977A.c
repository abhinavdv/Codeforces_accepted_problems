int function(number,subs)
{
    if (number % 10 >= subs)
    {
        printf("%d", number - subs);
        return 0;
    }
    else
    {
        subs = subs - number % 10 - 1;
        number = number / 10;
        function(number,subs);
    }
}
    int main()
    {
        int number, subs;
        scanf("%d%d", &number, &subs);
        function(number,subs);

    }
