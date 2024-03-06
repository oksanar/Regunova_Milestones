import sys
import requests
from URLSearchParams import URLSearchParams


API_BASE_URL = 'http://127.0.0.1:8001'


def get_birthdays(month_name: str, department: str):
    url = URLSearchParams(f'{API_BASE_URL}/birthdays')
    url = url.append({'month': month_name, 'department': department})
    response = requests.get(url)
    if not response.ok:
        return {
            'message': response.reason,
            'status_code': response.status_code
        }
    return response.json()


def get_anniversaries(month_name: str, department: str):
    url = URLSearchParams(f'{API_BASE_URL}/anniversaries')
    url = url.append({'month': month_name, 'department': department})
    response = requests.get(url)
    if not response.ok:
        return {
            'message': response.reason,
            'status_code': response.status_code
        }
    return response.json()


def get_report(month_name: str, department: str):
    birthdays = get_birthdays(month_name, department)
    anniversaries = get_anniversaries(month_name, department)
    report = ''
    if birthdays:
        report += f'Report for {department} department for {month_name.capitalize()} fetched.\n'
        report += f'Total {birthdays["total"]}, Anniversaries: {anniversaries["total"]}\n'
        anniversaries_map = {}
        if anniversaries['total'] > 0:
            for item in anniversaries['employees']:
                anniversaries_map[item['id']] = item
        if birthdays['total'] > 0:
            report += 'Employees:\n'
            for item in birthdays['employees']:
                is_anniversary = anniversaries_map.get(item['id'])
                if is_anniversary:
                    report += f"- {item['birthday']} ({item['age']}), {item['name']} (is anniversary)\n"
                else:
                    report += f"- {item['birthday']} ({item['age']}), {item['name']}\n"

    return report


if __name__ == '__main__':
    arg = sys.argv[1:]
    arg_len = len(arg)
    if arg_len < 2:
        raise ValueError('''Please provide month name and department.
As Example:
python3 fetch_report.py april "R&D"
        ''')
    month_name = arg[0]
    department = arg[1]
    report = get_report(month_name, department)
    print(report)
