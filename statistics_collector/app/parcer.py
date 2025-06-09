import asyncio
from datetime import datetime

from statistics_collector.database.models import ReturnToWork
from statistics_collector.dependencies import client
from statistics_collector.utils import save_stat_record, clear_table


async def parse_stat():
    queues = ["NWOCG", "NWOF", "NWOB", "NWOCG", "NWOM", "ENGEEJL"]

    from_date = "2025-01-01"
    to_date = datetime.now().strftime("%Y-%m-%d")

    await clear_table(ReturnToWork)

    for queue in queues:
        print('Обрабатываю', queue)
        issues = client.issues.find(
            filter={
                'queue': queue,
                'created': {'from': from_date, 'to': to_date}
            },
        )

        for issue in issues:
            changes = issue.changelog.get_all()._data
            counter = 0

            for change in changes:
                for field_change in change['fields']:
                    if (
                            field_change['field'].id == 'status'
                            and (field_change.get('from').key if field_change.get('from') else None) == 'testing'
                            and (field_change.get('to').key if field_change.get('to') else None) == 'inProgress'
                    ):
                        counter += 1

            await save_stat_record({
                'queue': queue,
                'priority': issue.priority.name if issue.priority else "",
                'type': issue.type.name if issue.type else "",
                'key': issue.key,
                'summary': issue.summary,
                'assignee': issue.assignee.display if issue.assignee else "Не назначен",
                'status': issue.status.display,
                'returns_to_work': counter
            }, ReturnToWork)


def test():
    print('qweqweqwe')


if __name__ == '__main__':
    asyncio.run(parse_stat())
