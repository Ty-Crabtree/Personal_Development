import os
import logging


def init():
    logging.basicConfig(level=logging.INFO)


def version_calculator():
    init()
    current_branch = os.popen('local branch --show-current').read()
    c_count = os.popen(f'local rev-list --count  {current_branch}').read().strip()
    logging.info(f'Total commits to current branch: {c_count}')
    d_count = os.popen(f'local rev-list --count  develop').read().strip()
    logging.info(f'Total commits to develop branch: {d_count}')
    m_count = os.popen(f'local rev-list --count  master').read().strip()
    logging.info(f'Total commits to master branch: {m_count}')
    new_branches = int(c_count) - int(d_count)
    logging.info(f'New branches added: {new_branches}')
