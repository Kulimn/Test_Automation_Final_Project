import allure

from extensions.verifications import Verifications
from workflow.api_flows import APIFlows

team_name = 'Sergey'
team_email = 'sergey@gmail.com'

class Test_API:
    @allure.title('Test01: Create Team & Verify Status Code')
    @allure.description('this test creates new team in Grafana')
    def test_create_and_verify_team(self):
        actual = APIFlows.create_team(team_name, team_email)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test02: Verify Team Nane')
    @allure.description('this test verifies the Grafana team name')
    def test_verify_team_member_name(self):
        nodes = ['teams', 0, 'name' ]
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name)

    @allure.title('Test03: Update Team & Verify Status Code')
    @allure.description('this test update team & verify status code')
    def test_update_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.update_team(team_name + 'Kiselov', team_email, id)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test04: Update Team Name')
    @allure.description('this test update team member name')
    def test_verify_team_update_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name +'Kiselov')

    @allure.title('Test05: Delete Team & Verify Status Code')
    @allure.description('this test delete team & verify status code')
    def test_delete_and_verify_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.delete_team(id)
        Verifications.verify_equals(actual, 200)




