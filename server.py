import json
import subprocess
import sys
import asyncio
from aiohttp import web
from pathlib import Path

LESSONS = json.loads(Path('lessons.json').read_text(encoding='utf-8'))


async def handle_run(request):
    data = await request.json()
    code = data.get('code', '')
    lesson_idx = data.get('lessonIndex', 0)

    lesson = LESSONS[lesson_idx]
    expected = lesson['expectedOutput'].strip()

    # Выполняем код в изолированной среде
    try:
        result = await asyncio.get_event_loop().run_in_executor(
            None, _exec_code, code
        )
    except Exception as e:
        return web.json_response({'success': False, 'output': str(e), 'expected': expected})

    output = result.strip()
    output_norm = '\n'.join(line.strip() for line in output.split('\n') if line.strip())
    expected_norm = '\n'.join(line.strip() for line in expected.split('\n') if line.strip())

    if output_norm == expected_norm:
        return web.json_response({'success': True, 'output': result})
    else:
        return web.json_response({'success': False, 'output': output, 'expected': expected})


def _exec_code(code):
    import io
    import sys
    captured = io.StringIO()
    old = sys.stdout
    sys.stdout = captured
    try:
        exec(code, {'__builtins__': __builtins__})
    except Exception:
        pass
    finally:
        sys.stdout = old
    return captured.getvalue()


def create_app():
    app = web.Application()
    app.router.add_post('/api/run', handle_run)
    app.router.add_static('/', Path(__file__).parent, name='static')
    return app


if __name__ == '__main__':
    web.run_app(create_app(), host='0.0.0.0', port=8080)
