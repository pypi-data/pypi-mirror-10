#compdef notsio

_notsio_books() {
    ( notsio books | cut -d' ' -f1 | xargs )
}

local -a _1st_arguments _2nd_arguments_notes
_1st_arguments=(
    'notes:Operate on notes stored on the server'
    'books:List all books on the server'
)

_2nd_arguments_notes=(
    'create:create a new note'
    'delete:delete one or more notes'
    'edit:edit a note in your favorite $EDITOR'
    'list:search or list notes'
    'modify:change one or more note attributes'
    'move-to:move one or more notes to another book'
    'show:show a note'
)

_arguments \
  '--version:show the version number' \
  '--debug:be more verbose' \
  '--quiet:do not output anything' \
  '--help:show help and exit' \
  '*:: :->subcmds' && return 0



if (( CURRENT == 1 ))
then
  _describe -t commands "notsio commands" _1st_arguments
  return


elif (( CURRENT == 2 ))
then
    case "$words[1]" in
        notes)
            _describe -t commands "notsio notes subcommands" _2nd_arguments_notes
            return
            ;;
    esac


else
    case "$words[2]" in
        create)
            _arguments \
                '--book::the book this note should be part of:($(_notsio_books))' \
                '--link:a valid url to store with this note:' \
                '*: :->forms' && return 0
            ;;
        list)
            _arguments \
                '--book::the book this note should be part of:($(_notsio_books))' \
                '--bookmarks:only show bookmarks' \
                '--no-bookmarks:do not show bookmarks' \
                '*: :->forms' &&  return 0
            ;;
        modify)
            _arguments \
                '--book::the book this note should be part of:($(_notsio_books))' \
                '--title::the title for this note' \
                '--link::a valid url to store with this note' \
                '*: :->forms' &&  return 0
            ;;
        move-to)
            _arguments \
                '1: :($(_notsio_books))' &&  return 0
            ;;
        show)
            _arguments \
                '--no-pager:do not pipe the output to $PAGER' \
                '*: :->forms' &&  return 0
            ;;
    esac
fi
