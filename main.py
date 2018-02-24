# -*- encoding: utf8 -*-
"""
generate icalendar file from lunar date
"""
import codecs
from argparse import ArgumentParser
from lunardate import LunarDate

def parse_args():
    parser = ArgumentParser(description=u"根据农历日期生成阳历的iCalendar文件，可以用于导入到outlook，google日历等。")
    parser.add_argument('lunar_date_file', help=u"农历日期文件，每行格式是:<事件标题>;<事件农历时间>")
    return parser.parse_args()

def parse_event_line(event_line):
    seps = event_line.split(';')
    if len(seps) != 2:
        return
    
    event_title = seps[0].strip()
    if not event_title:
        return
    
    event_date = seps[1].strip()
    if not event_date:
        return
    try:
        year = int(event_date[0:4])
        month = int(event_date[4:6])
        day = int(event_date[6:8])
    except Exception:
        return
    
    return (event_title, year, month, day)

def parse_event_file(event_file):
    """
    return event date list in format of 
    
    [(event_title, year, month, day), ... ]
    """
    events = []
    with codecs.open(event_file, 'r', encoding='utf-8') as fp:
        for line in fp:
            line = line.strip()
            event = parse_event_line(line)
            if event:
                events.append(event)
            elif line:
                print "[warning]this line cannot be parsed: %s" % line
    return events

def main():
    args = parse_args()
    events = parse_event_file(args.lunar_date_file)
    print events
    solardate = LunarDate(2017,11,29).toSolarDate()
    print solardate


if __name__ == "__main__":
    main()