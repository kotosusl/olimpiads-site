<template>
    <el-cascader :options="options" :show-all-levels="false" />
  </template>
  
  <script lang="ts" setup>
  const options = [
    {
      value: 'shcool_class',
      label: 'Class',
      children: [
        {value: '1', label: '1'}, {value: '2', label: '2'}, {value: '3', label: '3'}, {value: '4', label: '4'}, {value: '5', label: '5'},
        {value: '6', label: '6'}, {value: '7', label: '7'}, {value: '8', label: '8'}, {value: '9', label: '9'}, {value: '10', label: '10'},
        {value: '11', label: '11'}]},
    {
        value: 'subjects',
        label: 'Subjects',
        children: [
            {value: 'technical', label: 'Technical'}, {value: 'lingvist', label: 'Lingvist'},
            {value: 'humanitar', label: 'Humanitar'}, {value: 'bio', label: 'Bio'}
          ],
        },
      ]
    
  </script>
  