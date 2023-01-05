from invoke import task

@task
def install_requirements(c, force=False):
    force_cmd = "--force" if force else ""
    c.run(f"ansible-galaxy install -r requirements.yml {force_cmd}", pty=True)

@task
def playbook_run(c, dry_run=False):
    check_cmd = "--check" if dry_run else ""
    c.run(
        f"""
            ansible-playbook -i hosts playbook.yml \
                --private-key ~/.ssh/other-hosts/ssh-key-2023-01-05.key \
                --diff \
                {check_cmd}
        """,
        pty=True,
    )
