Ansible
=======

My ansible playbooks. Store some daily practice


# 逻辑语法

* only_if : 
```
- name: Test only_if
  command: w
  only_if: "'1' in $numbers"
```
* when :
```
- get_url: url=http://deb.goaccess.io/gnugpg.key dest=/var/keys/goaccess_signing.key
  register: result

- stat: path=/etc/ok
  register: check_ok

- command: apt-key add /var/keys/goaccess_signing.key
  when: result.changed and check_ok.stat.exists == false
```
