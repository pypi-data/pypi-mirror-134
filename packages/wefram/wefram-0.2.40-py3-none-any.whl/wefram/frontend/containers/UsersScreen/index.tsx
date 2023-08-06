import React, {createRef} from 'react'
import {
  Box,
  Dialog,
  EntityList,
  Typography
} from 'system/components'
import {LockOpen, Lock} from '@mui/icons-material'
import {ScreenProps} from 'system/types'
import {gettext} from 'system/l10n'
import {api} from 'system/api'
import {RequestApiPath} from 'system/routing'
import {UserCard} from '../UserCard'

const objectsPath: RequestApiPath = api.entityPath('system', 'User')


type UsersScreenState = {
  entityKey?: string | null
}


export default class UsersScreen extends React.Component<ScreenProps> {
  state: UsersScreenState = {
    entityKey: undefined
  }

  private listRef = createRef<EntityList>()

  render() {
    return (
      <React.Fragment>
      <Box mt={2}>
        <Typography variant={'h4'} paddingBottom={2}>{gettext("Administrate users", 'system.aaa')}</Typography>
        <EntityList
          ref={this.listRef}

          addButtonAction={() => this.setState({entityKey: null})}
          defaultSort={{value: 'fullName', direction: 'asc'}}
          deleteButton={true}
          deleteConfirmMessage={gettext("Are you sure you want to delete the selected users?", 'system.aaa-messages')}
          entityCaption={gettext("Users list", 'system.aaa')}
          limit={25}
          pagination
          primaryField={'fullName'}
          requestPath={objectsPath}
          sortOptions={[
            {value: 'login', caption: gettext("Login", 'system.aaa-list')},
            {value: 'fullName', caption: gettext("Full name", 'system.aaa-list')}
          ]}
          search
          secondaryField={[
            [
              {
                fieldType: 'boolean',
                fieldName: 'locked',
                hidden: (value: any): boolean => !Boolean(value),
                valueVisualize: (value: any): any => {
                  return value
                    ? (<Lock fontSize={'small'} style={{color: 'red'}}/>)
                    : (<LockOpen fontSize={'small'} style={{color: 'gray'}}/>)
                }
              },
              'login',
              {
                fieldType: 'dateTimeNice',
                fieldName: 'lastLogin',
                caption: gettext("Last logged on", 'system.aaa-list')
              }
            ],
          ]}
          selectable
          textTotalCount
          urlStateOffset
          urlStateSearch
          onItemClick={(item: any) => {
            this.setState({entityKey: item.id})
          }}
        />
      </Box>
      <Dialog open={this.state.entityKey !== undefined} maxWidth={'sm'}>
        {this.state.entityKey !== undefined && (
          <UserCard
            entityKey={this.state.entityKey}
            onClose={() => {
              this.setState({entityKey: undefined})
            }}
            onAfterDelete={() => {
              this.listRef.current?.update()
              this.setState({entityKey: undefined})
            }}
            onAfterSubmit={() => {
              this.listRef.current?.update()
              this.setState({entityKey: undefined})
            }}
          />
        )}
      </Dialog>
      </React.Fragment>
    )
  }
}
