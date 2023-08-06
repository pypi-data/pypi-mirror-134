====================
pytest-bugtong-tag
====================

=============
Installation
=============


To install pytest-bugtong-tag:

    $pip install pytest-bugtong-tag


Usage
=====

    .. code-block:: bash

        $pytest --tags=smoke

        $pytest --tags=smoke,xxx


Demo
====

    .. code-block:: bash

        @pytest.mark.tags(["smoke","abc"])
        def test_one():
            assert True

    