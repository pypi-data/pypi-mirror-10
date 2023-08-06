========
Usage
========

To use Decision table in a project::

        table = decisionTable.DecisionTable("""
            packageState     configState     config        action        new_packageState    new_configState
            ================================================================================================
            None             None            False         install       install             install            
            ok               ok              False         purge         purge               purge
            .                .               True          purge         ok                  purge
            .                .               True          update        ok                  update
            ok               error           False         purge         purge               purge
            .                .               True          update        ok                  update
            .                .               True          install       ok                  install
            .                .               True          purge         ok                  purge
            error            install         False         purge         purge               purge
            .                .               False         install       install             install
            None             error           True          purge         None                purge
            error            purge           False         purge         purge               purge
            ok               None            True          install       ok                  install
            .                .               False         purge         purge               None
            *                *               *             *             ERROR               ERROR
        """)
    
        new_packageState,new_configState = table.decision(
            ['new_packageState','new_configState'],
            packageState = 'error',
            configState = 'install',
            config = 'False',
            action = 'install'
        )
    
        print(new_packageState,new_configState)
        #(install,install)