'''importing the utility methods'''
from utility.actions import validateTeamHasOnlyFourForeignPlayers, validateOnlyOneWicketKeeper

def test_validateTeamHasOnlyFourForeignPlayers():
    '''test to validate that the team has only 4 foreign players'''
    assert validateTeamHasOnlyFourForeignPlayers() == 4

def test_validateOnlyOneWicketKeeper():
    '''test to validate that the team has only 1 wicket-keeper'''
    assert validateOnlyOneWicketKeeper() == 1

def test_boundaryValuesOnTeamForeignPlayers():
    '''test to validate the boundary values that the team has only 4 foreign players'''
    assert not validateTeamHasOnlyFourForeignPlayers() == 5
    assert not validateTeamHasOnlyFourForeignPlayers() == 3

def test_boundaryValuesOnTeamWicketKeepers():
    '''test to validate the boundary values that the team has only 1 wicket keeper'''
    assert not validateOnlyOneWicketKeeper() == 0
    assert not validateOnlyOneWicketKeeper() == 2


'''calling the test methods'''
'''positive tests'''
test_validateTeamHasOnlyFourForeignPlayers()
test_validateOnlyOneWicketKeeper()
'''negative tests'''
test_boundaryValuesOnTeamForeignPlayers()
test_boundaryValuesOnTeamWicketKeepers()
