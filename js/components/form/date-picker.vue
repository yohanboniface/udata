<style lang="less">
.date-picker {
    .dropdown-menu {
        min-width:100%;
        width:auto;
    }
}
</style>

<template>
<div class="input-group dropdown date-picker" :class="{ 'open': picking }"
    v-outside="onOutside">
    <span class="input-group-addon"><span class="fa fa-calendar"></span></span>
    <input type="text" class="form-control" v-el:input
        @focus="onFocus"
        :placeholder="placeholder"
        :required="required"
        :value="value|dateFormatted"
        :readonly="readonly"></input>
    <div class="dropdown-menu dropdown-menu-right">
        <calendar :selected="value"></calendar>
    </div>
    <input type="hidden" v-el:hidden
        :id="field.id"
        :name="serializable ? field.id : ''"
        :value="value"></input>
</div>
</template>

<script>
import moment from 'moment';
import Calendar from 'components/calendar.vue';

const DEFAULT_FORMAT = 'L';
const ISO_FORMAT = 'YYYY-MM-DDTHH:mm:ss';

export default {
    name: 'date-picker',
    replace: true,
    mixins: [require('components/form/base-field').FieldComponentMixin],
    props: {
        serializable: {
            type: Boolean,
            default: true
        }
    },
    components: {Calendar},
    data() {
        return {
            picking: false,
        };
    },
    filters: {
        dateFormatted(value) {
            // Will default to current day if value is null or empty.
            return value
                   ? moment(value).format(this.field.format || DEFAULT_FORMAT)
                   : '';
        }
    },
    events: {
        'calendar:date:selected': function(date) {
            this.$els.input.value = date.format(this.field.format || DEFAULT_FORMAT);
            this.$els.hidden.value = date.format(ISO_FORMAT);
            this.picking = false;
            return true;
        },
        'calendar:date:cleared': function() {
            this.$els.input.value = '';
            this.$els.hidden.value = '';
            this.picking = false;
            return true;
        }
    },
    methods: {
        onFocus() {
            this.picking = true;
        },
        onOutside() {
            this.picking = false;
        }
    }
};
</script>
