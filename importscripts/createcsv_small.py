import csv
import click

def geometricSum(x,n):
    return int(round((1-pow(x,n))/(1-x)))

@click.command()
@click.option('--usersperteam', '-upt', default=5, help='Average number of users per Team')
@click.option('--resourcesperteam', '-rpt', default=5, help='Number of resources per Team')
@click.option('--hierarchies', '-h', default=10, help='Number of Team hierarchies, must be > 0')
@click.option('--childteams', '-ct', default=3, help='Number of child teams')
def create_csv(usersperteam, resourcesperteam, hierarchies, childteams):

    numberOfTeams = geometricSum(childteams, hierarchies)

    #  NODES
    # Create Team nodes file
    startIdTeam = 0
    with open('smallgraph/Team.csv', 'w') as teamFile:
        fieldnames = ['teamId', 'name', 'type']
        writer = csv.DictWriter(teamFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'teamId':1,'name':'Redis Labs','type':'Team'})
        writer.writerow({'teamId':2,'name':'Modules Team','type':'Team'})

    startIdUser = startIdTeam + 2
    # Create User nodes file
    with open('smallgraph/User.csv', 'w') as userFile:
        fieldnames = ['userId', 'name', 'type']
        writer = csv.DictWriter(userFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'userId':1,'name':'Yiftach Schoolman','type':'User'})
        writer.writerow({'userId':2,'name':'Roi Lipman','type':'User'})
        writer.writerow({'userId':3,'name':'Pieter Cailliau','type':'User'})
        writer.writerow({'userId':4,'name':'Itamar Haber','type':'User'})
        writer.writerow({'userId':5,'name':'Jeffrey Lovitz','type':'User'})
        writer.writerow({'userId':6,'name':'Keren Ouaknine','type':'User'})

    startIdResource = startIdUser + 6
    # Create Resource node file
    with open('smallgraph/Resource.csv', 'w') as resourceFile:
        fieldnames = ['resourceId', 'name', 'type']
        writer = csv.DictWriter(resourceFile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'resourceId':1,'name':'New Year Party Pictures','type':'Resource'})
        writer.writerow({'resourceId':2,'name':'github.com/./RedisGraph','type':'Resource'})

    #  RELATIONSHIPS
    # user to team
    with open('smallgraph/PART_OF_TEAM.csv', 'w') as partOfTeamFile:
        writer = csv.writer(partOfTeamFile)
        writer.writerow([1+(startIdUser-1),1+(startIdTeam-1)])
        writer.writerow([2+(startIdUser-1),2+(startIdTeam-1)])
        writer.writerow([3+(startIdUser-1),2+(startIdTeam-1)])
        writer.writerow([4+(startIdUser-1),2+(startIdTeam-1)])
        writer.writerow([5+(startIdUser-1),2+(startIdTeam-1)])
        writer.writerow([6+(startIdUser-1),2+(startIdTeam-1)])
    # team to team
        writer.writerow([2+(startIdTeam-1),1+(startIdTeam-1)])

    # Each team has acces to {resources per team}
    with open('smallgraph/RESOURCE_ACCESS.csv', 'w') as resourceAccessFile:
        writer = csv.writer(resourceAccessFile)
        writer.writerow([1+(startIdTeam-1),1+(startIdResource-1)])
        writer.writerow([2+(startIdTeam-1),2+(startIdResource-1)])

if __name__ == '__main__':
  create_csv()
