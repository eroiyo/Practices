function gradingStudents(grades) {
    var result = []
    for (var i=0; i<grades.length; i++)
    {
        let x=grades[i];
        if(x<=37)
        {
         result.push(x)
        }else
        {
            let original=x;
            let e=3;
            let flag=false
            while(e>0)
            {
                if(x % 5 ==0){
                result.push(x)
                flag=true
                }
                x=x+1
                e=e-1
            }
            if(flag==false)
            {
                result.push(original)
            }
        }
    }
return result
}