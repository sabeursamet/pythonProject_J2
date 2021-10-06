from behave import given,when, then

@given(u'user is in url page https://qavbox.github.io/demo/dragndrop/')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user is in url page https://qavbox.github.io/demo/dragndrop/')


@given(u'two boxes appeared')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given two boxes appeared')


@when(u'user select "Drag" Box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user select "Drag" Box')


@when(u'Drop it to "Drop here" box')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Drop it to "Drop here" box')


@then(u'Dropped text appears')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Dropped text appears')
