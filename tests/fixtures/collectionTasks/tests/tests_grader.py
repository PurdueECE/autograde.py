import unittest
import collectionTasks as tasks


# Used for this Prelab ONLY.
emptyGUID = "96E4A421-B3C1-4BC5-9AAB-7FDB20EC82E2"


class TestGetComponentCountByProject(unittest.TestCase):
    def test_missingProjectID(self):
        self.assertRaises(ValueError, tasks.getComponentCountByProject, emptyGUID, "R")

    def test_ProjectID1(self):
        expectedValue = 83
        actualValue = tasks.getComponentCountByProject(
            "17A946D3-A1B0-4335-8808-8594D9FBD62C", "R"
        )
        self.assertEqual(expectedValue, actualValue)

    def test_ProjectID2(self):
        expectedValue = 74
        actualValue = tasks.getComponentCountByProject(
            "DE06228A-0544-4543-9055-A39D19DEDFA4", "C"
        )
        self.assertEqual(expectedValue, actualValue)

    def test_ProjectID3(self):
        expectedValue = 75
        actualValue = tasks.getComponentCountByProject(
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9", "I"
        )
        self.assertEqual(expectedValue, actualValue)

    def test_ProjectID4(self):
        expectedValue = 77
        actualValue = tasks.getComponentCountByProject(
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300", "T"
        )
        self.assertEqual(expectedValue, actualValue)


class TestGetComponentCountByStudent(unittest.TestCase):
    def test_MissingStudent(self):
        self.assertRaises(
            ValueError, tasks.getComponentCountByStudent, "Doo, Scooby", "R"
        )

    def test_Student1(self):
        expectedValue = 10
        actualValue = tasks.getComponentCountByStudent("Cook, Margaret", "R")
        self.assertEqual(expectedValue, actualValue)

    def test_Student2(self):
        expectedValue = 31
        actualValue = tasks.getComponentCountByStudent("Robinson, Pamela", "C")
        self.assertEqual(expectedValue, actualValue)

    def test_Student3(self):
        expectedValue = 30
        actualValue = tasks.getComponentCountByStudent("Scott, Michael", "I")
        self.assertEqual(expectedValue, actualValue)

    def test_Student4(self):
        expectedValue = 16
        actualValue = tasks.getComponentCountByStudent("Lopez, Juan", "T")
        self.assertEqual(expectedValue, actualValue)


class TestGetParticipationByStudent(unittest.TestCase):
    def test_MissingStudent(self):
        self.assertRaises(ValueError, tasks.getParticipationByStudent, "Doo, Scooby")

    def test_Student1(self):
        expectedValue = {
            "66FA081D-D1AA-4306-8650-9C39429CCDAB",
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9",
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "83383848-1D69-40D4-A360-817FB22769ED",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A",
            "2E7649C2-574A-496A-850B-F15190031E11",
            "8E56417E-0D81-4F43-8137-F1F7AA005654",
            "77A1A82E-749E-43BF-B3BF-3E70F087F808",
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300",
            "D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371",
            "32B9E998-97C3-4D5A-8005-C9685A08196F",
            "7C376AFE-6D98-4E50-B29C-71FBF6260B2D",
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            "90BE0D09-1438-414A-A38B-8309A49C02EF",
            "96CC6F98-B44B-4FEB-A06B-390432C1F6EA",
            "082D6241-40EE-432E-A635-65EA8AA374B6",
            "075A54E6-530B-4533-A2E4-A15226BE588C",
        }
        actualValue = tasks.getParticipationByStudent("Mitchell, Judith")
        self.assertSetEqual(expectedValue, actualValue)

    def test_Student2(self):
        expectedValue = {
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9",
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287",
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A",
            "2E7649C2-574A-496A-850B-F15190031E11",
            "77A1A82E-749E-43BF-B3BF-3E70F087F808",
            "FE647EE2-2EBD-4837-83F0-256C377365FE",
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300",
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            "8E56417E-0D81-4F43-8137-F1F7AA005654",
            "90BE0D09-1438-414A-A38B-8309A49C02EF",
            "96CC6F98-B44B-4FEB-A06B-390432C1F6EA",
            "32B9E998-97C3-4D5A-8005-C9685A08196F",
            "08EDAB1A-743D-4B62-9446-2F1C5824A756",
        }
        actualValue = tasks.getParticipationByStudent("Gonzalez, Kimberly")
        self.assertSetEqual(expectedValue, actualValue)

    def test_Student3(self):
        expectedValue = {
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9",
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "83383848-1D69-40D4-A360-817FB22769ED",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
            "D88C2930-9DA4-431F-8CDB-99A2AA2C7A05",
            "2E7649C2-574A-496A-850B-F15190031E11",
            "FE647EE2-2EBD-4837-83F0-256C377365FE",
            "075A54E6-530B-4533-A2E4-A15226BE588C",
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300",
            "7C376AFE-6D98-4E50-B29C-71FBF6260B2D",
            "90BE0D09-1438-414A-A38B-8309A49C02EF",
            "96CC6F98-B44B-4FEB-A06B-390432C1F6EA",
            "32B9E998-97C3-4D5A-8005-C9685A08196F",
            "08EDAB1A-743D-4B62-9446-2F1C5824A756",
        }
        actualValue = tasks.getParticipationByStudent("Ward, Sandra")
        self.assertSetEqual(expectedValue, actualValue)

    def test_Student4(self):
        expectedValue = {
            "66FA081D-D1AA-4306-8650-9C39429CCDAB",
            "D88C2930-9DA4-431F-8CDB-99A2AA2C7A05",
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A",
            "8C71F259-ECA8-4267-A8B3-6CAD6451D4CC",
            "8E56417E-0D81-4F43-8137-F1F7AA005654",
            "77A1A82E-749E-43BF-B3BF-3E70F087F808",
            "FE647EE2-2EBD-4837-83F0-256C377365FE",
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300",
            "7C376AFE-6D98-4E50-B29C-71FBF6260B2D",
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            "35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA",
            "08EDAB1A-743D-4B62-9446-2F1C5824A756",
        }
        actualValue = tasks.getParticipationByStudent("Russell, Scott")
        self.assertSetEqual(expectedValue, actualValue)


class TestGetParticipationByProject(unittest.TestCase):
    def test_MissingProjectID(self):
        self.assertRaises(ValueError, tasks.getParticipationByProject, emptyGUID)

    def test_ProjectID1(self):
        expectedValue = {
            "Stewart, Earl",
            "Jackson, Doris",
            "Jenkins, Paul",
            "Torres, Betty",
            "Perez, Kathleen",
            "Henderson, Christopher",
            "Baker, Craig",
            "Edwards, Rachel",
            "Martin, Richard",
            "Lee, Julie",
            "Sanchez, Deborah",
            "Garcia, Martha",
            "Young, Frank",
            "Martinez, David",
            "Peterson, Daniel",
            "Lopez, Juan",
            "Flores, Andrea",
            "Watson, Martin",
            "Foster, Benjamin",
            "Johnson, Roger",
            "Hill, Jose",
            "Hernandez, Lawrence",
            "Bennett, Nancy",
            "Campbell, Eugene",
            "Gray, Tammy",
            "Ramirez, Linda",
            "Collins, Anthony",
            "Jones, Stephanie",
            "Russell, Scott",
            "Perry, Marie",
            "Cooper, Kelly",
            "Miller, Aaron",
            "Moore, John",
            "Diaz, Tina",
            "Simmons, Cynthia",
            "Wood, Kevin",
            "Gonzales, Arthur",
            "Bryant, Evelyn",
            "Morris, Heather",
            "Williams, Mary",
            "Ross, Frances",
            "Gonzalez, Kimberly",
            "Long, Joshua",
            "Brooks, Carol",
            "Lewis, William",
            "Taylor, Brian",
            "Walker, Terry",
            "Green, Roy",
            "Turner, Theresa",
            "Patterson, Peter",
            "Butler, Julia",
            "Wilson, Howard",
            "Sanders, Emily",
            "Murphy, Donna",
            "Cook, Margaret",
            "Carter, Sarah",
            "Rogers, Elizabeth",
            "Richardson, George",
            "Griffin, Charles",
            "Barnes, Sean",
        }
        actualValue = tasks.getParticipationByProject(
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287"
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_ProjectID2(self):
        expectedValue = {
            "Stewart, Earl",
            "Harris, Anne",
            "Jackson, Doris",
            "Jenkins, Paul",
            "Brown, Robert",
            "Rodriguez, Jeffrey",
            "Torres, Betty",
            "Nelson, Louise",
            "Thomas, Mark",
            "Henderson, Christopher",
            "Baker, Craig",
            "Edwards, Rachel",
            "Martin, Richard",
            "White, Diana",
            "King, Carolyn",
            "Martinez, David",
            "Lopez, Juan",
            "Flores, Andrea",
            "Rivera, Patricia",
            "Watson, Martin",
            "Foster, Benjamin",
            "Johnson, Roger",
            "Hill, Jose",
            "Bennett, Nancy",
            "Reed, Bobby",
            "Campbell, Eugene",
            "Washington, Annie",
            "Gray, Tammy",
            "Kelly, Joyce",
            "Collins, Anthony",
            "Mitchell, Judith",
            "Russell, Scott",
            "Perry, Marie",
            "Miller, Aaron",
            "Bailey, Catherine",
            "Hall, Beverly",
            "Diaz, Tina",
            "Simmons, Cynthia",
            "Wood, Kevin",
            "Bryant, Evelyn",
            "Williams, Mary",
            "Alexander, Carlos",
            "Ross, Frances",
            "Robinson, Pamela",
            "Gonzalez, Kimberly",
            "Parker, Raymond",
            "Turner, Theresa",
            "Walker, Terry",
            "Green, Roy",
            "Patterson, Peter",
            "Butler, Julia",
            "Wilson, Howard",
            "Cox, Shirley",
            "Wright, Eric",
            "Sanders, Emily",
            "James, Randy",
            "Murphy, Donna",
            "Lowe, Karen",
            "Anderson, Debra",
            "Coleman, Lori",
        }
        actualValue = tasks.getParticipationByProject(
            "77A1A82E-749E-43BF-B3BF-3E70F087F808"
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_ProjectID3(self):
        expectedValue = {
            "Stewart, Earl",
            "Harris, Anne",
            "Jackson, Doris",
            "Jenkins, Paul",
            "Brown, Robert",
            "Rodriguez, Jeffrey",
            "Thomas, Mark",
            "White, Diana",
            "Lee, Julie",
            "Young, Frank",
            "Garcia, Martha",
            "Martinez, David",
            "Adams, Keith",
            "Watson, Martin",
            "Foster, Benjamin",
            "Johnson, Roger",
            "Hill, Jose",
            "Hernandez, Lawrence",
            "Bennett, Nancy",
            "Reed, Bobby",
            "Kelly, Joyce",
            "Collins, Anthony",
            "Price, Dorothy",
            "Russell, Scott",
            "Perry, Marie",
            "Cooper, Kelly",
            "Miller, Aaron",
            "Bailey, Catherine",
            "Hall, Beverly",
            "Moore, John",
            "Thompson, Michelle",
            "Phillips, Brenda",
            "Wood, Kevin",
            "Bryant, Evelyn",
            "Morris, Heather",
            "Davis, Douglas",
            "Williams, Mary",
            "Ross, Frances",
            "Robinson, Pamela",
            "Gonzalez, Kimberly",
            "Brooks, Carol",
            "Taylor, Brian",
            "Walker, Terry",
            "Wilson, Howard",
            "James, Randy",
            "Murphy, Donna",
            "Ward, Sandra",
            "Lowe, Karen",
            "Carter, Sarah",
            "Rogers, Elizabeth",
            "Richardson, George",
            "Hughes, James",
        }
        actualValue = tasks.getParticipationByProject(
            "FE647EE2-2EBD-4837-83F0-256C377365FE"
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_ProjectID4(self):
        expectedValue = {
            "Stewart, Earl",
            "Morgan, Edward",
            "Harris, Anne",
            "Jenkins, Paul",
            "Brown, Robert",
            "Rodriguez, Jeffrey",
            "Perez, Kathleen",
            "Nelson, Louise",
            "Thomas, Mark",
            "Henderson, Christopher",
            "Scott, Michael",
            "Baker, Craig",
            "Edwards, Rachel",
            "Martin, Richard",
            "White, Diana",
            "Powell, Gregory",
            "Lee, Julie",
            "Garcia, Martha",
            "Evans, Johnny",
            "Lopez, Juan",
            "Watson, Martin",
            "Rivera, Patricia",
            "Hill, Jose",
            "Griffin, Charles",
            "Bennett, Nancy",
            "Washington, Annie",
            "Howard, Shawn",
            "Kelly, Joyce",
            "Collins, Anthony",
            "Mitchell, Judith",
            "Jones, Stephanie",
            "Price, Dorothy",
            "Perry, Marie",
            "Cooper, Kelly",
            "Phillips, Brenda",
            "Simmons, Cynthia",
            "Wood, Kevin",
            "Gonzales, Arthur",
            "Bryant, Evelyn",
            "Williams, Mary",
            "Ross, Frances",
            "Gonzalez, Kimberly",
            "Long, Joshua",
            "Smith, Jimmy",
            "Lewis, William",
            "Turner, Theresa",
            "Walker, Terry",
            "Green, Roy",
            "Allen, Amanda",
            "Patterson, Peter",
            "Sanders, Emily",
            "James, Randy",
            "Ward, Sandra",
            "Rogers, Elizabeth",
            "Richardson, George",
            "Coleman, Lori",
            "Roberts, Teresa",
        }
        actualValue = tasks.getParticipationByProject(
            "2E7649C2-574A-496A-850B-F15190031E11"
        )
        self.assertSetEqual(expectedValue, actualValue)


class TestGetCostOfProjects(unittest.TestCase):
    def test_getCostOfProjects(self):
        expectedValue = {
            "082D6241-40EE-432E-A635-65EA8AA374B6": 245.46,
            "90BE0D09-1438-414A-A38B-8309A49C02EF": 335.16,
            "96CC6F98-B44B-4FEB-A06B-390432C1F6EA": 268.48,
            "FE647EE2-2EBD-4837-83F0-256C377365FE": 213.73,
            "77A1A82E-749E-43BF-B3BF-3E70F087F808": 369.48,
            "83383848-1D69-40D4-A360-817FB22769ED": 367.49,
            "8E56417E-0D81-4F43-8137-F1F7AA005654": 262.39,
            "56B13184-D087-48DB-9CBA-84B40FE17CC5": 355.36,
            "66FA081D-D1AA-4306-8650-9C39429CCDAB": 256.63,
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300": 388.81,
            "17A946D3-A1B0-4335-8808-8594D9FBD62C": 295.25,
            "075A54E6-530B-4533-A2E4-A15226BE588C": 358.84,
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A": 292.63,
            "D88C2930-9DA4-431F-8CDB-99A2AA2C7A05": 428.72,
            "8C71F259-ECA8-4267-A8B3-6CAD6451D4CC": 325.13,
            "2E7649C2-574A-496A-850B-F15190031E11": 304.08,
            "32B9E998-97C3-4D5A-8005-C9685A08196F": 400.34,
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9": 350.93,
            "7C376AFE-6D98-4E50-B29C-71FBF6260B2D": 249.63,
            "35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA": 394.44,
            "D230BAC0-249C-410F-84E4-41F9EDBFCB20": 235.24,
            "D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371": 241.42,
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9": 334.98,
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287": 370.65,
            "DE06228A-0544-4543-9055-A39D19DEDFA4": 375.37,
            "B9C94766-617A-4168-B2AA-44FFE8323E32": 231.96,
            "6CCCA5F3-3008-46FF-A779-2D2F872DAF82": 233.6,
            "08EDAB1A-743D-4B62-9446-2F1C5824A756": 376.4,
        }

        actualValue = tasks.getCostOfProjects()
        self.assertDictEqual(expectedValue, actualValue)


class TestGetProjectByComponent(unittest.TestCase):
    def test_ComponentGroup1(self):
        expectedValue = {
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9",
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300",
            "7C376AFE-6D98-4E50-B29C-71FBF6260B2D",
            "90BE0D09-1438-414A-A38B-8309A49C02EF",
            "96CC6F98-B44B-4FEB-A06B-390432C1F6EA",
            "32B9E998-97C3-4D5A-8005-C9685A08196F",
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A",
            "2E7649C2-574A-496A-850B-F15190031E11",
            "D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371",
            "35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA",
            "8E56417E-0D81-4F43-8137-F1F7AA005654",
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "83383848-1D69-40D4-A360-817FB22769ED",
            "8C71F259-ECA8-4267-A8B3-6CAD6451D4CC",
            "77A1A82E-749E-43BF-B3BF-3E70F087F808",
            "FE647EE2-2EBD-4837-83F0-256C377365FE",
            "D230BAC0-249C-410F-84E4-41F9EDBFCB20",
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287",
            "082D6241-40EE-432E-A635-65EA8AA374B6",
            "075A54E6-530B-4533-A2E4-A15226BE588C",
            "08EDAB1A-743D-4B62-9446-2F1C5824A756",
            "6CCCA5F3-3008-46FF-A779-2D2F872DAF82",
            "D88C2930-9DA4-431F-8CDB-99A2AA2C7A05",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
            "B9C94766-617A-4168-B2AA-44FFE8323E32",
            "56B13184-D087-48DB-9CBA-84B40FE17CC5",
        }

        actualValue = tasks.getProjectByComponent(
            {"ALQ-409", "MCB-906", "AVL-897", "LPQ-301"}
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_ComponentGroup2(self):
        expectedValue = {
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9",
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300",
            "96CC6F98-B44B-4FEB-A06B-390432C1F6EA",
            "32B9E998-97C3-4D5A-8005-C9685A08196F",
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A",
            "2E7649C2-574A-496A-850B-F15190031E11",
            "D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371",
            "35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA",
            "8E56417E-0D81-4F43-8137-F1F7AA005654",
            "66FA081D-D1AA-4306-8650-9C39429CCDAB",
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "83383848-1D69-40D4-A360-817FB22769ED",
            "8C71F259-ECA8-4267-A8B3-6CAD6451D4CC",
            "77A1A82E-749E-43BF-B3BF-3E70F087F808",
            "FE647EE2-2EBD-4837-83F0-256C377365FE",
            "D230BAC0-249C-410F-84E4-41F9EDBFCB20",
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287",
            "075A54E6-530B-4533-A2E4-A15226BE588C",
            "08EDAB1A-743D-4B62-9446-2F1C5824A756",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
            "B9C94766-617A-4168-B2AA-44FFE8323E32",
            "56B13184-D087-48DB-9CBA-84B40FE17CC5",
        }
        actualValue = tasks.getProjectByComponent(
            {"LRV-843", "TCC-914", "LRZ-850", "UQC-346"}
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_ComponentGroup3(self):
        expectedValue = {
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9",
            "7C376AFE-6D98-4E50-B29C-71FBF6260B2D",
            "90BE0D09-1438-414A-A38B-8309A49C02EF",
            "32B9E998-97C3-4D5A-8005-C9685A08196F",
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A",
            "2E7649C2-574A-496A-850B-F15190031E11",
            "D7EFB850-9A34-41B0-BD9D-FBCDF4C3C371",
            "35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA",
            "8E56417E-0D81-4F43-8137-F1F7AA005654",
            "66FA081D-D1AA-4306-8650-9C39429CCDAB",
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "83383848-1D69-40D4-A360-817FB22769ED",
            "8C71F259-ECA8-4267-A8B3-6CAD6451D4CC",
            "77A1A82E-749E-43BF-B3BF-3E70F087F808",
            "FE647EE2-2EBD-4837-83F0-256C377365FE",
            "D230BAC0-249C-410F-84E4-41F9EDBFCB20",
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287",
            "08EDAB1A-743D-4B62-9446-2F1C5824A756",
            "075A54E6-530B-4533-A2E4-A15226BE588C",
            "6CCCA5F3-3008-46FF-A779-2D2F872DAF82",
            "D88C2930-9DA4-431F-8CDB-99A2AA2C7A05",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
            "B9C94766-617A-4168-B2AA-44FFE8323E32",
            "56B13184-D087-48DB-9CBA-84B40FE17CC5",
        }
        actualValue = tasks.getProjectByComponent(
            {"TEG-078", "PBT-741", "KSL-520", "ULR-468"}
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_ComponentGroup4(self):
        expectedValue = {
            "177EBF38-1C20-497B-A2EF-EC1880FEFDF9",
            "4C5B295B-58E1-4CFB-80DF-88938B9A6300",
            "7C376AFE-6D98-4E50-B29C-71FBF6260B2D",
            "90BE0D09-1438-414A-A38B-8309A49C02EF",
            "32B9E998-97C3-4D5A-8005-C9685A08196F",
            "0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A",
            "35C50EBA-E3A9-4AB7-A67C-64D4228C4DCA",
            "8E56417E-0D81-4F43-8137-F1F7AA005654",
            "66FA081D-D1AA-4306-8650-9C39429CCDAB",
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "8C71F259-ECA8-4267-A8B3-6CAD6451D4CC",
            "77A1A82E-749E-43BF-B3BF-3E70F087F808",
            "FE647EE2-2EBD-4837-83F0-256C377365FE",
            "D230BAC0-249C-410F-84E4-41F9EDBFCB20",
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            "3BB1CF3F-79B7-4AFC-95D8-FDEA4FAE9287",
            "082D6241-40EE-432E-A635-65EA8AA374B6",
            "075A54E6-530B-4533-A2E4-A15226BE588C",
            "08EDAB1A-743D-4B62-9446-2F1C5824A756",
            "6CCCA5F3-3008-46FF-A779-2D2F872DAF82",
            "56B13184-D087-48DB-9CBA-84B40FE17CC5",
        }
        actualValue = tasks.getProjectByComponent(
            {"ROJ-198", "CLO-275", "DCE-568", "CGV-812"}
        )
        self.assertSetEqual(expectedValue, actualValue)


class TestGetCommonByProject(unittest.TestCase):
    def test_MissingProjectID1(self):  # 1 Point
        self.assertRaises(
            ValueError,
            tasks.getCommonByProject,
            emptyGUID,
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
        )

    def test_MissingProjectID2(self):  # 1 Point
        self.assertRaises(
            ValueError,
            tasks.getCommonByProject,
            "DE06228A-0544-4543-9055-A39D19DEDFA4",
            emptyGUID,
        )

    def test_ProjectPair1(self):  # 1.5 Point
        expectedValue = [
            "ACB-546",
            "ALK-605",
            "ART-641",
            "AVT-730",
            "BFC-689",
            "BLT-317",
            "BOT-567",
            "BRT-517",
            "BTP-574",
            "CCT-418",
            "CCW-596",
            "CDT-350",
            "CFI-435",
            "CIA-184",
            "CJF-903",
            "CKN-960",
            "CLQ-971",
            "CMN-194",
            "CNT-391",
            "CPF-254",
            "CRV-843",
            "CTL-054",
            "CTM-765",
            "CUI-564",
            "CUP-407",
            "CYK-835",
            "CZD-741",
            "DLU-953",
            "EBR-839",
            "ERK-824",
            "ERV-630",
            "EVC-461",
            "FCC-018",
            "FLK-572",
            "GLC-746",
            "GUL-971",
            "GZT-093",
            "HBR-310",
            "HOR-267",
            "HOR-269",
            "HOT-036",
            "HRI-734",
            "IBC-258",
            "ICK-271",
            "ICV-048",
            "IGT-143",
            "ILM-531",
            "ITB-681",
            "ITR-486",
            "JLG-916",
            "JNL-870",
            "JRL-310",
            "JSC-743",
            "JTM-187",
            "KFR-508",
            "KSL-520",
            "KTQ-835",
            "KUR-213",
            "LBR-792",
            "LCD-472",
            "LDR-679",
            "LHU-967",
            "LIB-281",
            "LIW-368",
            "LJR-923",
            "LKY-561",
            "LMW-349",
            "LTF-192",
            "LVU-609",
            "LWY-204",
            "LXY-873",
            "MCQ-163",
            "MLJ-635",
            "MLW-452",
            "MRL-546",
            "NCT-205",
            "NOC-324",
            "NRL-517",
            "NUR-482",
            "OCN-506",
            "ORV-075",
            "OUT-239",
            "PDL-589",
            "PEC-560",
            "PWR-658",
            "QHR-752",
            "QSC-941",
            "RBP-254",
            "RJC-490",
            "RJW-851",
            "RKP-916",
            "RLJ-147",
            "RLV-754",
            "RMC-692",
            "RMY-042",
            "ROT-791",
            "ROZ-908",
            "RQO-067",
            "RSH-743",
            "RST-279",
            "RSV-145",
            "RTI-590",
            "RTN-652",
            "RUO-978",
            "RUY-876",
            "SLT-025",
            "SRB-504",
            "TAZ-349",
            "TCH-815",
            "TED-127",
            "TED-890",
            "THJ-397",
            "TIJ-568",
            "TLQ-234",
            "TLR-058",
            "TOC-798",
            "TOM-325",
            "TPB-798",
            "TQJ-016",
            "TRT-985",
            "TSW-590",
            "TTV-390",
            "TTV-875",
            "TWC-459",
            "TXS-069",
            "TYT-809",
            "TYV-928",
            "UCR-095",
            "UNL-746",
            "URT-903",
            "USC-781",
            "VCM-206",
            "VLN-472",
            "VSR-074",
            "WTU-670",
            "WZL-635",
            "XOT-130",
            "XQR-965",
            "XRY-260",
            "XRZ-943",
            "YDR-391",
            "YLF-462",
            "YQC-438",
            "YRT-026",
            "YSR-096",
            "YWT-432",
            "ZDL-529",
            "ZWR-028",
        ]
        actualValue = tasks.getCommonByProject(
            "6E30ADB2-7AD0-4E22-8A78-96135AAD7BD9",
            "83383848-1D69-40D4-A360-817FB22769ED",
        )
        self.assertListEqual(expectedValue, actualValue)

    def test_ProjectPair2(self):  # 1.5 Point
        expectedValue = [
            "ACT-109",
            "ARL-318",
            "AVL-897",
            "AVT-730",
            "BCK-438",
            "BHT-805",
            "BKT-189",
            "BMC-621",
            "BOT-567",
            "BRC-613",
            "BTY-690",
            "CBU-096",
            "CDT-350",
            "CGC-827",
            "CJF-903",
            "CLF-372",
            "CLY-417",
            "CLZ-560",
            "CMN-194",
            "CNM-019",
            "CNT-459",
            "CPO-768",
            "CRV-843",
            "CTL-054",
            "CYK-835",
            "CYS-314",
            "DKR-948",
            "DRS-986",
            "DRZ-594",
            "EBR-839",
            "ECX-418",
            "FCI-290",
            "FCR-469",
            "FER-167",
            "FLK-572",
            "GCC-589",
            "GCL-489",
            "GLE-706",
            "GQT-421",
            "GRU-310",
            "GTV-294",
            "HFT-317",
            "HRI-734",
            "HRK-348",
            "IHC-318",
            "IOL-306",
            "JCT-492",
            "JRS-260",
            "KLF-473",
            "KRU-458",
            "KTW-062",
            "KXR-640",
            "LAG-958",
            "LAI-791",
            "LDH-439",
            "LDO-368",
            "LFD-103",
            "LGU-172",
            "LIA-019",
            "LKW-419",
            "LLW-108",
            "LNF-713",
            "LOK-793",
            "LPD-814",
            "LPZ-362",
            "LQW-368",
            "LTF-192",
            "LVZ-021",
            "LXI-173",
            "LYO-125",
            "MRL-546",
            "NCT-205",
            "NUR-482",
            "OLN-178",
            "ORW-143",
            "OTT-587",
            "PLR-243",
            "PSR-183",
            "PWR-658",
            "QJC-162",
            "QTA-356",
            "RAR-965",
            "RAV-941",
            "RCL-035",
            "RFY-461",
            "RGR-687",
            "RHE-256",
            "RHN-426",
            "RIK-619",
            "RIV-940",
            "RJC-490",
            "RJH-485",
            "RKP-916",
            "RLJ-147",
            "RPF-751",
            "RQO-067",
            "RSO-480",
            "RSV-145",
            "RTF-418",
            "RTI-590",
            "RTZ-759",
            "RUY-876",
            "RVE-754",
            "RYN-509",
            "RZU-625",
            "SFR-674",
            "SJL-465",
            "SMC-379",
            "SQR-671",
            "SRN-491",
            "TAK-481",
            "TAZ-349",
            "TBE-891",
            "TBM-508",
            "TCC-914",
            "TJD-632",
            "TOM-325",
            "TQJ-016",
            "TRW-692",
            "TVL-127",
            "TXC-972",
            "TYB-523",
            "TYV-928",
            "UCH-710",
            "UCT-021",
            "UEL-264",
            "UTH-014",
            "VCQ-412",
            "VFL-589",
            "VLS-582",
            "VMR-152",
            "VOL-042",
            "WHT-289",
            "WHT-451",
            "WTJ-148",
            "WTV-158",
            "WTX-053",
            "XLD-638",
            "XQR-965",
            "XRY-260",
            "YBT-782",
            "YRJ-074",
            "YRT-026",
            "YUT-624",
            "ZTN-927",
            "ZWR-028",
        ]
        actualValue = tasks.getCommonByProject(
            "56B13184-D087-48DB-9CBA-84B40FE17CC5",
            "17A946D3-A1B0-4335-8808-8594D9FBD62C",
        )
        self.assertListEqual(expectedValue, actualValue)


#    def test_getComponentReport(self):
#        def test_Component Group 1(self):
#            expectedValue = {'AGC-216': 19, 'FER-167': 14, 'GZT-093': 24, 'ROQ-034': 3, 'TJD-632': 20}
#
#            actualValue = tasks.getComponentReport({'GZT-093', 'FER-167', 'TJD-632', 'ROQ-034', 'AGC-216'})
#            self.assertDictEqual(expectedValue, actualValue)
#
#        def test_Component Group 2(self):
#            expectedValue = {'HOR-267': 40, 'ILT-213': 37, 'LPD-814': 20, 'WTU-670': 16, 'YDR-391': 20}
#            actualValue = tasks.getComponentReport({'ILT-213', 'WTU-670', 'HOR-267', 'YDR-391', 'LPD-814'})
#            self.assertDictEqual(expectedValue, actualValue)


class TestGetCircuitByStudent(unittest.TestCase):
    def test_StudentGroup1(self):
        expectedValue = {
            "49-9-44",
            "43-7-85",
            "29-9-59",
            "64-3-62",
            "65-2-28",
            "56-7-60",
            "23-5-51",
            "75-9-27",
            "15-1-06",
            "34-4-26",
            "83-0-13",
            "24-9-46",
            "42-0-02",
            "14-5-82",
            "76-3-95",
            "30-8-14",
            "69-8-80",
            "39-1-11",
            "42-0-45",
            "63-2-99",
            "58-0-62",
            "57-2-62",
            "93-1-30",
            "85-6-78",
            "15-0-37",
            "10-0-55",
            "48-2-41",
            "53-1-29",
            "52-6-35",
            "69-1-62",
            "88-4-47",
            "49-6-69",
            "61-0-09",
            "91-0-61",
            "22-3-50",
            "76-7-84",
            "58-8-81",
            "86-8-58",
            "45-8-13",
            "97-6-19",
        }

        actualValue = tasks.getCircuitByStudent(
            {
                "Evans, Johnny",
                "Martinez, David",
                "Perry, Marie",
                "Diaz, Tina",
                "Simmons, Cynthia",
            }
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_StudentGroup2(self):
        expectedValue = {
            "21-1-59",
            "72-9-11",
            "63-2-68",
            "59-3-63",
            "15-1-06",
            "88-6-24",
            "46-1-68",
            "54-9-43",
            "60-4-31",
            "59-3-49",
            "52-5-93",
            "63-9-60",
            "53-9-58",
            "52-9-50",
            "55-8-29",
            "63-8-72",
            "72-2-22",
            "90-0-76",
            "40-4-41",
            "67-4-02",
            "15-0-37",
            "10-2-91",
            "57-8-26",
            "33-7-38",
            "34-4-81",
            "75-1-93",
            "47-9-78",
            "69-1-62",
            "14-4-77",
            "55-8-34",
            "61-1-25",
            "78-7-77",
            "68-0-63",
            "32-2-34",
            "91-0-61",
            "46-7-61",
            "84-2-05",
        }
        actualValue = tasks.getCircuitByStudent(
            {
                "Garcia, Martha",
                "Watson, Martin",
                "Clark, Joe",
                "Morris, Heather",
                "Davis, Douglas",
            }
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_StudentGroup3(self):
        expectedValue = {
            "49-9-44",
            "51-8-46",
            "11-9-49",
            "29-9-59",
            "21-2-69",
            "15-1-06",
            "40-0-23",
            "51-0-75",
            "46-1-68",
            "81-0-43",
            "30-8-14",
            "69-8-80",
            "43-2-02",
            "39-1-11",
            "63-8-72",
            "67-3-59",
            "85-6-78",
            "25-6-48",
            "53-1-29",
            "48-8-76",
            "45-9-48",
            "38-6-08",
            "77-3-57",
            "90-0-05",
            "41-0-17",
            "81-7-77",
            "68-0-63",
            "58-8-81",
            "97-6-19",
            "39-3-99",
        }
        actualValue = tasks.getCircuitByStudent(
            {
                "Diaz, Tina",
                "Bryant, Evelyn",
                "Alexander, Carlos",
                "Cook, Margaret",
                "Baker, Craig",
            }
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_StudentGroup4(self):
        expectedValue = {
            "40-4-46",
            "91-1-23",
            "23-5-51",
            "75-9-27",
            "59-6-05",
            "75-9-18",
            "28-0-26",
            "54-9-43",
            "52-5-93",
            "76-3-95",
            "92-7-57",
            "43-2-02",
            "42-0-45",
            "58-0-62",
            "16-7-59",
            "55-7-20",
            "65-3-93",
            "15-0-37",
            "10-0-55",
            "57-8-26",
            "81-5-42",
            "33-5-22",
            "19-6-11",
            "89-2-73",
            "52-6-35",
            "14-4-77",
            "88-4-47",
            "30-6-36",
            "70-7-77",
            "41-0-17",
            "73-1-31",
            "61-0-09",
            "75-8-48",
            "89-8-16",
            "22-1-53",
            "91-0-61",
            "74-1-27",
            "13-3-04",
            "26-4-54",
            "35-7-32",
        }
        actualValue = tasks.getCircuitByStudent(
            {
                "Mitchell, Judith",
                "Allen, Amanda",
                "Thompson, Michelle",
                "Simmons, Cynthia",
                "Carter, Sarah",
            }
        )
        self.assertSetEqual(expectedValue, actualValue)


class TestGetCircuitByComponent(unittest.TestCase):
    def test_ComponentGroup1(self):
        expectedValue = {
            "41-9-83",
            "81-7-77",
            "85-8-63",
            "39-2-25",
            "18-5-39",
            "18-6-26",
            "69-3-16",
            "59-6-05",
            "72-2-22",
            "66-8-55",
            "74-6-61",
            "55-7-20",
            "85-6-78",
            "26-7-85",
            "66-8-19",
        }

        actualValue = tasks.getCircuitByComponent(
            {"TOA-748", "CIK-821", "KFC-238", "VML-389", "CCE-431"}
        )
        self.assertSetEqual(expectedValue, actualValue)

    def test_ComponentGroup2(self):
        expectedValue = {
            "90-1-33",
            "29-9-59",
            "18-5-39",
            "21-2-69",
            "91-1-23",
            "75-9-18",
            "66-8-19",
            "42-0-02",
            "97-7-38",
            "52-5-93",
            "51-4-82",
            "42-0-45",
            "57-2-62",
            "10-2-91",
            "55-3-42",
            "49-5-44",
            "49-6-69",
            "77-3-73",
            "91-0-61",
            "39-3-07",
            "74-6-61",
        }
        actualValue = tasks.getCircuitByComponent(
            {"CQL-174", "LKX-209", "YVL-845", "ZHR-274", "GUL-971"}
        )
        self.assertSetEqual(expectedValue, actualValue)


if __name__ == "__main__":
    unittest.main()
