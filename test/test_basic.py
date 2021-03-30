import pytest

from armaclass import parse


def test_empty():
    expected = {'Moo': {}}
    result = parse('class Moo {};')
    assert result == expected


# We're not really deleting anything, just acknowledging the command to delete an object
def test_delete():
    expected = {'Foo': {}}
    result = parse(
        'class Foo {\r\ndelete Moo; };')
    assert result == expected


def test_integer_property():
    expected = {
        'Moo': {
            'value': 1
        }
    }
    result = parse('class Moo {\r\nvalue=1; };')
    assert result == expected


def test_more_than_one_value_in_file():
    expected = {
        'version': 12,
        'Moo': {
            'value': 1
        }
    }
    result = parse('version=12;\n\nclass Moo  {\r\n value = 1; };')
    assert result == expected


def test_array_of_scalars():
    expected = {
        'Moo': {
            'foo': ['bar', 'baz', 1.5e2]
        }
    }
    result = parse('class Moo {\r\nfoo[]={"bar", "baz",1.5e2}; };')
    assert result == expected


def test_scientific_notation():
    assert parse('x=-1.5e2;') == {'x': -1.5e2}


def test_plus_array():
    expected = {'Moo': {
        'foo': [1, 2, 3]
    }}
    result = parse(
        'class Moo {\r\nfoo[] += {1,2,3}; };')
    assert result == expected

# def test_simple_arithmetic(self):
#     assert parse('x=48+0x800;'), {'x': 48 + 0x800})


def test_ignore_symbols():
    test_string = (
        'class Moo {\n'
        '\tfoo = xxx;\n'
        '\tclass xxx {};\n'
        '};'
    )
    with pytest.raises(RuntimeError):
        parse(test_string)


def test_ignore_inheritance():
    test_string = 'class Moo : foo {};'
    assert parse(test_string) == {'Moo': {}}


def test_line_comments():
    assert parse('// foo comment') == {}
    assert parse('// foo comment\nx=2;') == {'x': 2}
    assert parse('x=2;// foo comment') == {'x': 2}
    assert parse('class Moo { // foo comment\n};') == {'Moo': {}}


def test_multiline_comments():
    assert parse('/* foo comment*/') == {}
    assert parse('/* foo comment\nsomething */x=2;') == {'x': 2}
    assert parse('x=2;/* foo comment*/') == {'x': 2}
    assert parse('x/*asd*/=/**/2;/* foo comment*/') == {'x': 2}
    assert parse('class Moo { /* foo comment*/};') == {'Moo': {}}


def test_quote_escaping_by_double_quote():
    assert parse('foo="bar ""haha"";";\n') == {'foo': 'bar "haha";'}


def test_sample():
    expected = {
        'Session': {
            'Player1': {
                'customScore': 0,
                'killed': 0,
                'killsAir': 0,
                'killsArmor': 0,
                'killsInfantry': 4,
                'killsPlayers': 0,
                'killsSoft': 0,
                'killsTotal': 4,
                'name': 'Lord DK'
            },
            'Player2': {
                'customScore': 0,
                'killed': 0,
                'killsAir': 0,
                'killsArmor': 0,
                'killsInfantry': 3,
                'killsPlayers': 0,
                'killsSoft': 0,
                'killsTotal': 3,
                'name': 'XiviD'
            },
            'Player3': {
                'customScore': 0,
                'killed': 0,
                'killsAir': 0,
                'killsArmor': 0,
                'killsInfantry': 2,
                'killsPlayers': 0,
                'killsSoft': 0,
                'killsTotal': 2,
                'name': '40mm2Die'
            },
            'Player4': {
                'customScore': 0,
                'killed': 0,
                'killsAir': 0,
                'killsArmor': 0,
                'killsInfantry': 4,
                'killsPlayers': 0,
                'killsSoft': 0,
                'killsTotal': 4,
                'name': 'WickerMan'
            },
            'Player5': {
                'customScore': 0,
                'killed': 1,
                'killsAir': 0,
                'killsArmor': 0,
                'killsInfantry': 3,
                'killsPlayers': 0,
                'killsSoft': -1,
                'killsTotal': 1,
                'name': 'Fusselwurm'
            },
            'Player6': {
                'customScore': 0,
                'killed': 0,
                'killsAir': 0,
                'killsArmor': 0,
                'killsInfantry': 0,
                'killsPlayers': 0,
                'killsSoft': 0,
                'killsTotal': 0,
                'name': 'Simmax'
            },
            'Player7': {
                'customScore': 0,
                'killed': 2,
                'killsAir': 0,
                'killsArmor': 0,
                'killsInfantry': 0,
                'killsPlayers': 0,
                'killsSoft': 0,
                'killsTotal': 0,
                'name': 'Andre'
            },
            'duration': 5821.1724,
            'gameType': 'Coop',
            'island': 'Altis',
            'mission': 'W-CO@10 StealBoot v03'
        }
    }
    result = parse('''
    class Session
    {
        mission="W-CO@10 StealBoot v03";
        island="Altis";
        gameType="Coop";
        duration=5821.1724;

        class Player1
        {
            name="Lord DK";
            killsInfantry=4;
            killsSoft=0;
            killsArmor=0;
            killsAir=0;
            killsPlayers=0;
            customScore=0;
            killsTotal=4;
            killed=0;
        };
        class Player2
        {
            name="XiviD";
            killsInfantry=3;
            killsSoft=0;
            killsArmor=0;
            killsAir=0;
            killsPlayers=0;
            customScore=0;
            killsTotal=3;
            killed=0;
        };
        class Player3
        {
            name="40mm2Die";
            killsInfantry=2;
            killsSoft=0;
            killsArmor=0;
            killsAir=0;
            killsPlayers=0;
            customScore=0;
            killsTotal=2;
            killed=0;
        };
        class Player4
        {
            name="WickerMan";
            killsInfantry=4;
            killsSoft=0;
            killsArmor=0;
            killsAir=0;
            killsPlayers=0;
            customScore=0;
            killsTotal=4;
            killed=0;
        };
        class Player5
        {
            name="Fusselwurm";
            killsInfantry=3;
            killsSoft=-1;
            killsArmor=0;
            killsAir=0;
            killsPlayers=0;
            customScore=0;
            killsTotal=1;
            killed=1;
        };
        class Player6
        {
            name="Simmax";
            killsInfantry=0;
            killsSoft=0;
            killsArmor=0;
            killsAir=0;
            killsPlayers=0;
            customScore=0;
            killsTotal=0;
            killed=0;
        };
        class Player7
        {
            name="Andre";
            killsInfantry=0;
            killsSoft=0;
            killsArmor=0;
            killsAir=0;
            killsPlayers=0;
            customScore=0;
            killsTotal=0;
            killed=2;
        };
    };
    ''')
    assert result == expected


def test_multiline_init():
    source = (
        r'class Item0 {'
        r'    position[]={1954.6425,5.9796591,5538.1045};'
        r'    id=0;'
        r'    init="[this, ""Platoon""] call FP_fnc_setVehicleName;" \n "if (isServer) then {" \n "  [this] call '
        r'FP_fnc_clearVehicle; this addWeaponCargoGlobal [""CUP_launch_M136"", 1];" \n "  this '
        r'addMagazineCargoGlobal [""1Rnd_HE_Grenade_shell"", 10];" \n "  this addMagazineCargoGlobal '
        r'[""ATMine_Range_Mag"", 6];" \n "};";'
        r'};'
    )

    result = parse(source)
    expected = {
        'Item0': {
            'position': [1954.6425, 5.9796591, 5538.1045],
            'id': 0,
            'init': '[this, "Platoon"] call FP_fnc_setVehicleName;\nif (isServer) then {\n  [this] call '
                    'FP_fnc_clearVehicle; this addWeaponCargoGlobal ["CUP_launch_M136", 1];\n  this '
                    'addMagazineCargoGlobal ["1Rnd_HE_Grenade_shell", 10];\n  this addMagazineCargoGlobal '
                    '["ATMine_Range_Mag", 6];\n};'
        }
    }
    assert result == expected
