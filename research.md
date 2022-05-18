# PythonFundamentals

## Research

### Sual 02

İnterpreter və Compiler dillər nədir?

#### Cavab

**Interpreter**

Interpreter translates just one statement of the program at a time into machine code. An interpreter takes very less time to analyze the source code. However, the overall time to execute the process is much slower. An interpreter does not generate an intermediary code. Hence, an interpreter is highly efficient in terms of its memory. Keeps translating the program continuously till the first error is confronted. If any error is spotted, it stops working and hence debugging becomes easy. Interpreters are used by programming languages like Ruby and Python for example.

**Compiler**

Compiler scans the entire program and translates the whole of it into machine code at once. A compiler takes a lot of time to analyze the source code. However, the overall time taken to execute the process is much faster. A compiler always generates an intermediary object code. It will need further linking. Hence more memory is needed. A compiler generates the error message only after it scans the complete program and hence debugging is relatively harder while working with a compiler. Compliers are used by programming languages like C and C++ for example.

### Sual 03

İmperative və declarative üslub nədir?

#### Cavab

**Imperative**

With **imperative** programming, you tell the compiler what you want to happen, step by step.

For example, let's start with this collection, and choose the odd numbers:

```C#
List<int> collection = new List<int> { 1, 2, 3, 4, 5 };
```

With **imperative** programming, we'd step through this, and decide what we want:

```C#
List<int> results = new List<int>();
foreach(var num in collection)
{  
    if (num % 2 != 0)
        results.Add(num);
}
```

Here, we're saying:

- Create a result collection
- Step through each number in the collection
- Check the number, if it's odd, add it to the results

**Declarative**

With **declarative** programming, on the other hand, you write code that describes what you want, but not necessarily how to get it (declare your desired results, but not the step-by-step):

```C#
var results = collection.Where( num => num % 2 != 0);
```

Here, we're saying "Give us everything where it's odd", not "Step through the collection. Check this item, if it's odd, add it to a result collection."

### Sual 04

Yeni proqramlaşdırma dilini öz başıma öyrənməli olsaydım nə edərdim?

#### Cavab

YouTube və s. kimi plsuz mənbələrdən istifaadə edərdim. Əsasən də YouTube da öyrəmək istədiyim proqramlaşdırma dilinin "crash course"lar izləyərdim və daha yaxşı başa düşmək üçün praktik olaraq öz öyrəndiklərimi tətbiq edərdim məsələlərə. Bununla həm nəzəri həm də praktii özümü inkişaf etdirərdim.

### Sual 05

Proqramlaşdırma dillərinin dizayn olunması deyiləndə ağlınıza nə gəlir? Yəni bir proqramlaşdırma dili necə dizayn edilə bilər?

#### Cavab

*Bu sualın cavabı uzun olduğu üçün oxuduğum mənbəni yerləşdirirəm.*
[Mənbə](http://ducklang.org/designing-a-programming-language-i)
