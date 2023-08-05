import React from 'react'
import {
  Chapters,
  Grid,
  TranslatedChapter,
  DateTimeText,
  EntityForm,
  FormPaper,
  FormItem,
  FormStoredImage,
  FormSwitchField,
  FormPasswordSetterField,
  FormTextInputField,
  StaticText,
  TipTypography,
  Typography
} from 'system/components'
import {gettext} from 'system/l10n'
import {api} from 'system/api'
import {RequestApiPath} from 'system/routing'
import {session, UserEditModel} from 'system/aaa'


const Help = () => (
  <Chapters>
    <TranslatedChapter appName={'system'} caption={gettext("Users", 'system')} textId={'help_usercard'} />
  </Chapters>
)


const objectPath: RequestApiPath = api.entityObjectPath('system', 'User')

type CardProps = {
  entityKey: string | null
  onAfterDelete: () => void
  onAfterSubmit: () => void
  onClose: () => void
}

type CardState = {
  data: UserEditModel
}


export default class Card extends React.Component<CardProps, CardState> {
  state: CardState = {
    data: {
      id: null,
      login: '',
      secret: '',
      locked: false,
      createdAt: null,
      lastLogin: null,
      firstName: "",
      middleName: "",
      lastName: "",
      timezone: null,
      locale: null,
      comments: '',
      fullName: "",
      avatar: null
    }
  }

  render() {
    const key: string | null = this.props.entityKey
    const requiredForSubmit: string[] =
      key === null && !this.state.data.login.includes('@')
      ? ['login', 'firstName', 'secret']
      : ['login', 'firstName']

    return (
      <EntityForm
        entityKey={key}
        requestPath={objectPath}

        data={this.state.data}
        help={<Help />}
        onUpdateData={(data, cb) => this.setState({data}, cb)}
        requiredForSubmit={requiredForSubmit}
        submitFieldsModel={[
          'login',
          'secret',
          'locked',
          'firstName',
          'middleName',
          'lastName',
          'timezone',
          'locale',
          'comments',
          'avatar'
        ]}

        submit
        delete={key !== null && (String(session.user?.id) !== String(key))}
        title={key === null ? gettext("New user", 'system.aaa-form') : this.state.data.fullName}
        windowed

        onAfterDelete={this.props.onAfterDelete}
        onAfterSubmit={this.props.onAfterSubmit}
        onClose={this.props.onClose}
      >
        {key !== null && (
          <FormPaper variant={'outlined'}>
            <FormItem width={6}>
              <StaticText caption={gettext("Last logon time", 'system.aaa-form')}>
                <DateTimeText value={this.state.data.lastLogin} />
              </StaticText>
            </FormItem>
            <FormItem width={6}>
              <StaticText caption={gettext("Created at")}>
                <DateTimeText value={this.state.data.createdAt} />
              </StaticText>
            </FormItem>
          </FormPaper>
        )}

        <Grid container spacing={'8px'}>
          <Grid item xs={4} display={'flex'} alignItems={'center'} justifyContent={'flex-start'}>
            <FormStoredImage
              cover
              entity={'system.users'}
              formName={'avatar'}
              imageSize={'200px'}
              variant={'rounded'}
              permitUpload
              permitClean
            />
          </Grid>
          <Grid item xs={8}>
            <FormPaper spacingBefore={0} spacingAfter={0}>
              <FormTextInputField
                error={this.state.data.login === ''}
                formName={'login'}
                label={gettext("Login", 'system.aaa-form')}
                required
                width={8}
              />
              <FormSwitchField
                disabled={String(session.user?.id) === String(key)}
                label={gettext("Is locked", 'system.aaa-form')}
                formName={'locked'}
                width={4}
              />
              {/*<FormItem width={12}>*/}
              {/*  <TipTypography>*/}
              {/*    This is just a test message*/}
              {/*  </TipTypography>*/}
              {/*</FormItem>*/}
              <FormTextInputField
                formName={'lastName'}
                label={gettext("Last name", 'system.aaa-form')}
                width={12}
              />
              <FormTextInputField
                error={this.state.data.firstName === ''}
                formName={'firstName'}
                label={gettext("First name", 'system.aaa-form')}
                required
                width={6}
              />
              <FormTextInputField
                formName={'middleName'}
                label={gettext("Middle name", 'system.aaa-form')}
                width={6}
              />
            </FormPaper>
          </Grid>
        </Grid>

        <FormPaper title={gettext("Password", 'system.aaa')}>
          {key !== null && (
            <FormItem width={12} >
              <Typography style={{fontSize: '.9rem'}}>
                {gettext("Type a new password to change it for the user", 'system.aaa-form')}
              </Typography>
            </FormItem>
          )}
          <FormPasswordSetterField
            labelPassword={gettext("Password", 'system.aaa-form')}
            labelConfirmation={gettext("Password confirmation", 'system.aaa-form')}
            formName={'secret'}
            spacing={2}
            clearable={this.state.data.login.includes('@')}
            width={12}
          />
          {key === null
              && (this.state.data.secret === null || this.state.data.secret === '')
              && (!this.state.data.login.includes('@'))
              &&
          (
            <FormItem pt={2} pb={2} width={12}>
              <Typography style={{
                fontSize: '.9rem',
                color: 'red'
              }}>
                {gettext("Password required to be set for the new user", 'system.aaa-form')}
              </Typography>
            </FormItem>
          )}
        </FormPaper>

        <FormPaper title={gettext("Details", 'system.aaa-form')}>
          <FormTextInputField
            formName={'comments'}
            label={gettext("Comments", 'system.aaa-form')}
            multiline
            width={12}
          />
        </FormPaper>
      </EntityForm>
    )
  }
}

