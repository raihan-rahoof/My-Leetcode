class Solution:
    def reformatDate(self, date: str) -> str:
        month={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05",          
        "Jun":"06","Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", 
        "Dec":"12"}

        d,m,y=date.split(" ")
        if len(d)==3:
            d="0"+d[0]
        else:
            d=d[:2]
        
        mm=month.get(m)

        day=y+"-"+mm+"-"+d

        return day