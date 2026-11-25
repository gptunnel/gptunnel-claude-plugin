#!/usr/bin/env python3
"""Static checks for the GPTunneL plugins. Run: python3 scripts/check.py (needs PyYAML)."""
import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def tool_set(name: str) -> set[str]:
    lines = (ROOT / 'tools' / name).read_text().splitlines()
    return {l.strip() for l in lines if l.strip() and not l.startswith('#')}


FULL = tool_set('full.txt')
CATALOG = tool_set('catalog.txt')
TOOL_RE = re.compile(r'`((?:lab|app|apps|gallery|list|get|create|update|delete|fork|run|upload|retry|reset|cancel|publish|set)_[a-z_]+|whoami)`')
# Backticked words that match the tool pattern but are params, not tools.
NOT_TOOLS = {'app_code'}

PLUGINS = {
    'gptunnel': {'tools': FULL, 'mcp_url': 'https://gptunnel.ru/mcp'},
    'gptunnel-claude': {'tools': CATALOG, 'mcp_url': 'https://gptunnel.ru/mcp/claude'},
}
# The catalog plugin must not offer to spend money or produce media (Anthropic directory policy 4(B)).
CATALOG_FORBIDDEN = re.compile(
    r'lab_generate|lab_quote|run_workflow|app_run|retry_node|max_cost_rub|'
    r'\bgenerate (an |a )?(image|video|picture|photo)|text-to-(image|video)|image generation|video generation',
    re.I,
)


def check_skills(plugin: str, cfg: dict) -> None:
    skills = sorted((ROOT / 'plugins' / plugin / 'skills').glob('*/SKILL.md'))
    if not skills:
        err(f'{plugin}: no skills')
    names = {p.parent.name for p in skills}
    for path in skills:
        rel = path.relative_to(ROOT)
        text = path.read_text()
        parts = text.split('---', 2)
        if len(parts) < 3 or parts[0].strip():
            err(f'{rel}: no YAML frontmatter')
            continue
        fm = yaml.safe_load(parts[1]) or {}
        desc = fm.get('description', '')
        if fm.get('name') != path.parent.name:
            err(f'{rel}: name "{fm.get("name")}" != folder "{path.parent.name}"')
        if 'Use when' not in desc:
            err(f'{rel}: description has no "Use when"')
        if 'NOT for' not in desc:
            err(f'{rel}: description has no "NOT for"')
        if len(desc) > 1024:
            err(f'{rel}: description is {len(desc)} chars (max 1024)')
        for other in re.findall(r'\(use ([a-z0-9]+-[a-z0-9-]+)', desc):
            if other not in names:
                err(f'{rel}: description points to missing skill "{other}"')
        if re.search(r'\d[\d.,]*\s?(₽|руб|RUB\b)', text):
            err(f'{rel}: hardcoded price — take prices from lab_quote / apps_list')
        for tool in set(TOOL_RE.findall(text)) - NOT_TOOLS:
            if tool not in cfg['tools']:
                err(f'{rel}: tool `{tool}` is not on this plugin\'s MCP surface')
        if plugin == 'gptunnel-claude':
            m = CATALOG_FORBIDDEN.search(text)
            if m:
                err(f'{rel}: catalog plugin mentions "{m.group(0)}"')


def load(path: pathlib.Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as e:  # noqa: BLE001
        err(f'{path.relative_to(ROOT)}: {e}')
        return {}


def check_manifests() -> None:
    version = (ROOT / 'VERSION').read_text().strip()
    found: dict[str, str] = {}
    mk = load(ROOT / '.claude-plugin/marketplace.json')
    found['.claude-plugin/marketplace.json metadata'] = mk.get('metadata', {}).get('version', '')
    for p in mk.get('plugins', []):
        found[f'.claude-plugin/marketplace.json {p["name"]}'] = p.get('version', '')
        if p.get('source') != './plugins/gptunnel':
            err('marketplace.json must list only ./plugins/gptunnel (the catalog plugin goes to the Anthropic directory)')
    cur = load(ROOT / '.cursor-plugin/marketplace.json')
    found['.cursor-plugin/marketplace.json'] = cur.get('metadata', {}).get('version', '')
    for rel in [
        'plugins/gptunnel/.claude-plugin/plugin.json',
        'plugins/gptunnel/plugin.json',
        'plugins/gptunnel/.cursor-plugin/plugin.json',
        'plugins/gptunnel-claude/.claude-plugin/plugin.json',
    ]:
        found[rel] = load(ROOT / rel).get('version', '')
    for where, v in found.items():
        if v != version:
            err(f'{where}: version "{v}" != VERSION "{version}"')

    for plugin, cfg in PLUGINS.items():
        mcp = load(ROOT / 'plugins' / plugin / '.mcp.json')
        url = mcp.get('mcpServers', {}).get('gptunnel', {}).get('url')
        if url != cfg['mcp_url']:
            err(f'plugins/{plugin}/.mcp.json: url {url} != {cfg["mcp_url"]}')
    portable = load(ROOT / 'plugins/gptunnel/mcp.json')
    if portable.get('mcpServers', {}).get('gptunnel', {}).get('url') != PLUGINS['gptunnel']['mcp_url']:
        err('plugins/gptunnel/mcp.json: url differs from .mcp.json')
    readme_root = (ROOT / 'README.md').read_text()
    for name in sorted(p.parent.name for p in (ROOT / 'plugins/gptunnel/skills').glob('*/SKILL.md')):
        if f'`{name}`' not in readme_root:
            err(f'README.md: skill `{name}` is not listed')


def check_directory_files() -> None:
    # Files the Anthropic directory accepts from non-Verified organizations: prose, JSON, PNG.
    allowed = {'.md', '.json', '.png', ''}
    base = ROOT / 'plugins' / 'gptunnel-claude'
    for f in base.rglob('*'):
        if f.is_file() and (f.suffix.lower() not in allowed or 'evals' in f.relative_to(base).parts):
            err(f'{f.relative_to(ROOT)}: not accepted in the Anthropic directory (only .md, .json, .png; no evals)')
    for plugin in PLUGINS:
        if (ROOT / 'plugins' / plugin / 'evals').exists():
            err(f'plugins/{plugin}/evals: keep evals in evals/{plugin}/')


check_manifests()
check_directory_files()
for plugin, cfg in PLUGINS.items():
    check_skills(plugin, cfg)

if errors:
    print('\n'.join(f'✗ {e}' for e in errors))
    sys.exit(1)
print('✔ all checks passed')
