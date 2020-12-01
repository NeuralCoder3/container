
import sys



data = list(map(lambda s: s.strip(),
    ("\n"+sys.stdin.read()+"\n")
    .replace("\n{","\n{\n")
    # .replace("}\n","\n}\n")
    .replace("\n\n","\n")
    .replace("\n\n","\n")
    .strip()
    .split("\n")))

def parseTree(data):
    content=""
    count=0
    while True:
        l=data[0]
        data=data[1:]
        if l=="{":
            contentAdd,data=parseTree(data)
            content+=contentAdd
            data=data[1:]
            count+=1
            continue
        if l.startswith("==") or l=="}":
            break
        content+="\\AxiomC{$"+l+"$}\n"
        count+=1

    rule="UnaryInfC"
    if count==0:
        content+="\\AxiomC{}\n"
    elif count==2:
        rule="BinaryInfC"
    elif count==3:
        rule="TrinaryInfC"
    elif count==4:
        rule="QuaternaryInfC"

    content+="\\"+rule+"{$"+data[0]+"$}\n"
    return content,data[1:]

content,_=parseTree(data)

content=r"""\begin{prooftree}"""+"\n"+content+r"""\end{prooftree}"""+"\n"

if len(sys.argv)>1:
    args=sys.argv[1].lower()
    if "s" in args:
        content=r"\scalebox{.7}{\parbox{1cm}{"+"\n"+content+r"}}"+"\n"
    if "c" in args:
        content=r"\begin{center}"+"\n"+content+r"\end{center}"+"\n"
    if "m" in args:
        content=r"\begin{minipage}[t]{.5\textwidth}"+"\n"+content+r"\end{minipage}"+""

print(content)